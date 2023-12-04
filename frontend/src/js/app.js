// Desc: Main JS file for the frontend

// Function to call at every page load
async function start(){
    // Initial updates when the page loads
    await processAccessToken();
    await updateRepoOptions();
    await updateTraceMethodOptions();
    syncSliderValue();
}
// Function to redirect to a new page
async function redirectToPage(page) {
    // window.location = page;
    window.open(page);
}

// ----------------------------------------

// Function to make an API request
async function makeApiRequest(apiUrl, selectedMethod, body, form) {

    // Get the access token from localStorage
    var accessToken = localStorage.getItem('access_token');
    
    if (!accessToken) {
        alert('No access token found in localStorage. Please Login first.');
        return;
    }
    var headers = new Headers();
    headers.append('Authorization', 'Bearer ' + accessToken);
    
    var data_GET = {
        method: selectedMethod,
        headers: headers,
    };
    var data_POST = {
        method: selectedMethod,
        headers: headers,
        body: body,
    };
    try {
        data = selectedMethod == 'GET' ? data_GET : data_POST;
        if (selectedMethod == 'POST' && !form) {
            data.body = JSON.stringify(body);
            data.headers.append('Content-Type', 'application/json');
        }
        const response = await fetch(apiUrl, data);
        if (response.status == 401) {
            console.log('Token expired or invalid. Please login again.');
            // redirectToPage('http://localhost:3000/api/auth/google');
            alert('Token expired or invalid. Please login again.');
        }
        response_body = await response.json();
        if (response.status != 200) {
            console.log('ResponseMakeApiRequest: ' + JSON.stringify(response_body) + response.status);
        }
        return {
            status: response.status,
            body: response_body
        }
    } catch (error) {
        // console.error("Error: ", error);
        console.log('Error, failed to make API request. -> ', error.message);
        throw error;
    }
}

// ----------------------------------------

// Function to check for an access token in the URL, store it in localStorage, and remove it from the URL
async function processAccessToken() {
    // Parse the query parameters of the URL
    var urlParams = new URLSearchParams(window.location.search);

    // Check if the URL contains an 'access_token' parameter
    if (urlParams.has('access_token')) {
        // Access token found, get its value
        var accessToken = urlParams.get('access_token');

        // Store the access token in localStorage
        localStorage.setItem('access_token', accessToken);

        // Remove the access token from the URL
        removeAccessTokenFromUrl();

        // Do something with the access token if needed
        console.log('Access Token:', accessToken);
    } else {
        // No access token found in the URL
        console.log('No Access Token found in the URL.');
    }
}

// Function to remove the 'access_token' parameter from the URL
function removeAccessTokenFromUrl() {
    // Get the current URL without query parameters
    var baseUrl = window.location.origin + window.location.pathname;

    // Replace the current URL without the 'access_token' parameter
    history.replaceState({}, document.title, baseUrl);
}

// ----------------------------------------

// Function to create a new repository and update the repository options
async function createRepoForm() {
    const createRepoForm = document.getElementById('createRepoForm');
    const repoDescriptionInput = createRepoForm.querySelector('#repo_owner');
    const repoOwner = repoDescriptionInput.value;
    const repoNameInput = createRepoForm.querySelector('#repo_name');
    const repoName = repoNameInput.value;
    // alert('Repo Owner: ' + repoOwner + ' Repo Name: ' + repoName);
    var body = {
        repo_owner: repoOwner,
        repo_name: repoName
    };
    // body = JSON.parse(JSON.stringify(body));
    // Add Creating... label to the form
    const creatingLabel = messageLabel('Creating...');
    createRepoForm.appendChild(creatingLabel);
    const response = await makeApiRequest('http://localhost:3000/api/repo', 'POST', body, false);
    if (response.status != 200) {
        console.log('ResponseCreateRepoForm: ' + JSON.stringify(response) + response.status);
        const failed = messageLabel('Failed to create repository.');
        createRepoForm.appendChild(failed);
        return;
    }
    // alert('ResponseCreateRepoForm: ' + JSON.stringify(response) + response.status);
    await updateRepoOptions();
    const success = messageLabel('Repository created.');
    createRepoForm.appendChild(success);
}

function messageLabel(message) {
    const oldMessageLabel = document.getElementById('messageLabel');
    if (oldMessageLabel){
        oldMessageLabel.remove();
    }
    const messageLabel = document.createElement('label');
    messageLabel.textContent = message;
    messageLabel.id = 'messageLabel';
    return messageLabel;
}

// Function to set the selected repository and update the artifact options
async function setRepo() {
    // Get the selected repository method from the form
    var selectedRepo = await getSelectedRepo();

    // Check if a repository method is selected
    if (selectedRepo) {
        // Save the selected repository method to localStorage
        localStorage.setItem('selected_repo', selectedRepo);

        // Optionally, perform additional actions or log the selection
        console.log('Selected Repository:', selectedRepo);
        // alert('Selected Repository: ' + selectedRepo);
        updateArtifactOptions('source');
        updateArtifactOptions('target');
        updateRepoDetailsSection();
    } else {
        // No repository method selected, you can handle this case accordingly
        console.warn('No Repository Selected');
    }
}

// Function to acquire the selected repository
async function getSelectedRepo() {
    // Get all radio buttons with the name 'existing_repos'
    var repoRadioButtons = document.getElementsByName('existing_repos');

    // Loop through the radio buttons to find the selected one
    for (var i = 0; i < repoRadioButtons.length; i++) {
        if (repoRadioButtons[i].checked) {
            // Return the value of the selected radio button
            return repoRadioButtons[i].value;
        }
    }

    // Return null if no radio button is selected
    return null;
}

// Function to update the options in the Select Repository form
async function updateRepoOptions() {
    // Clear the selected repository from localStorage
    localStorage.removeItem('selected_repo');

    const selectRepoForm = document.getElementById('selectRepoForm');
    const repoOptionsContainer = selectRepoForm.querySelector('.scrollable-options');

    // Clear existing options
    repoOptionsContainer.innerHTML = '';

    // Fetch updated repository list
    const response = await makeApiRequest('http://localhost:3000/api/repo', 'GET', null, false);
    // alert('Response updateRepoOptions: ' + JSON.stringify(response));

    // Add options based on the fetched data
    repos = response.body.repos;
    repos.forEach(repo => {
        const option = document.createElement('div');
        option.classList.add('form-check');
        repo_combined = repo.split('.')[0] + '/' + repo.split('.')[1];
        option.innerHTML = `
            <input class="form-check-input" type="radio" name="existing_repos" id="${repo}" value="${repo}">
            <label class="form-check-label" for="${repo}">
                ${repo_combined}
            </label>
        `;
        repoOptionsContainer.appendChild(option);
    });
}

//  ----------------------------------------

// Function to populate a repository with github artifacts and given requirements file
async function populateRepo(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    var populateRepoForm = document.getElementById('populateRepoForm');
    var selectedRepo = localStorage.getItem('selected_repo');
    var selectedFile = await getSelectedFile();
    if (!selectedFile) {
        alert('No file selected');
        return;
    }
    const uri = 'http://localhost:3000/api/repo/' + selectedRepo + '/populate';

    // Create a FormData object to handle the file and other form data
    var formData = new FormData();
    formData.append('requirements_file', selectedFile);

    const populatingLabel = messageLabel('Populating...');
    populateRepoForm.appendChild(populatingLabel);
    const response = await makeApiRequest(uri, 'POST', formData, true);
    updateArtifactOptions('source');
    updateArtifactOptions('target');
    if (response.status != 200) {
        console.log('ResponsePopulateRepo: ' + JSON.stringify(response) + response.status);
        const failed = messageLabel('Failed to populate repository.');
        populateRepoForm.appendChild(failed);
        return;
    }
    // alert('Repo populated.');
    const success = messageLabel('Repository populated.');
    populateRepoForm.appendChild(success);
    updateRepoDetailsSection();
}

// Function to get the selected file
async function getSelectedFile() {
    var fileInput = document.getElementById('file');
    // Check if a file is selected
    if (fileInput && fileInput.files.length > 0) {
        // Access the selected file
        var selectedFile = fileInput.files[0];

        // You can now use 'selectedFile' as needed, for example, log its details
        console.log('Selected File:', selectedFile);

        // Optionally, perform additional actions with the selected file
        return selectedFile;
    } else {
        // No file selected, you can handle this case accordingly
        console.warn('No File Selected');
        return null;
    }
}

// ----------------------------------------

// Function to make a create trace links request
async function createTraceLinks(event) {
    event.preventDefault();
    var createTraceLinksForm = document.getElementById('createTraceLinks');
    var selectedRepo = localStorage.getItem('selected_repo');
    var selectedSourceArtifact = document.getElementById('sourceSelectedArtifact').value;
    var selectedTargetArtifact = document.getElementById('targetSelectedArtifact').value;
    var selectedTraceMethod = document.getElementById('selectedTraceMethod').value;
    var selectedThreshold = document.getElementById('selectedThreshold').value;
    if (!selectedRepo) {
        alert('No repo selected');
        return;
    }
    if (!selectedSourceArtifact) {
        alert('No source artifact selected');
        return;
    }
    if (!selectedTargetArtifact) {
        alert('No target artifact selected');
        return;
    }
    if (!selectedTraceMethod) {
        alert('No trace method selected');
        return;
    }
    const uri = 'http://localhost:3000/api/repo/' + selectedRepo + '/trace';
    console.log(selectedSourceArtifact + ' ' + selectedTargetArtifact + ' ' + selectedTraceMethod)
    var body = {
        'source_artifact_type': selectedSourceArtifact,
        'target_artifact_type': selectedTargetArtifact,
        'trace_method': selectedTraceMethod,
        'threshold': selectedThreshold
    };
    var creatingLabel = messageLabel('Creating...');
    createTraceLinksForm.appendChild(creatingLabel);
    const response = await makeApiRequest(uri, 'POST', body, false);
    if (response.status != 200) {
        console.log('ResponseCreateTraceLinks: ' + JSON.stringify(response) + response.status);
        const failed = messageLabel('Failed to create trace links.');
        return;
    }
    // const resultMessage = document.getElementById('resultMessage');
    // resultMessage.innerHTML = 'Trace links created.';
    const num_of_links = response.body.num_of_links;
    successMessage = num_of_links + ' trace links created.';
    const success = messageLabel(successMessage);
    createTraceLinksForm.appendChild(success);
    // alert(num_of_links + ' trace links created.');
    updateRepoDetailsSection();
}

// Function to update the artifact options
async function updateArtifactOptions(type) {
    const buttonsElement = type + 'ArtifactButtons';
    const selectedElement = type + 'SelectedArtifact';
    const buttonTypeElement = type + '-btn-group-artifacts';

    const artifactButtons = document.getElementById(buttonsElement);
    artifactButtons.innerHTML = '';
    repo = localStorage.getItem('selected_repo');
    if (!repo) {
        alert('No repo selected');
        return;
    }
    // Fetch trace method options
    const uri = 'http://localhost:3000/api/repo/' + repo + '/artifacts';
    const response = await makeApiRequest(uri, 'GET', null, false);

    artifactOptions = response.body.artifact_types;

    artifactOptions.forEach(option => {
        const button = document.createElement('button');
        button.type = 'button';
        button.classList.add('btn', 'btn-outline-primary', buttonTypeElement);
        button.textContent = option;
        button.addEventListener('click', function () {
            // Toggle the active class and update the hidden input
            const allButtons = document.getElementsByClassName(buttonTypeElement);
            for (const otherButton of allButtons) {
                otherButton.classList.remove('active');
            }
            button.classList.toggle('active');
            const selectedArtifactInput = document.getElementById(selectedElement);
            selectedArtifactInput.value = button.classList.contains('active') ? option : '';
        });
        artifactButtons.appendChild(button);
    });
}

// Function to update the trace method options
async function updateTraceMethodOptions() {
    const traceMethodButtons = document.getElementById('traceMethodButtons');

    // Clear existing options
    traceMethodButtons.innerHTML = '';

    const response = await makeApiRequest('http://localhost:3000/api/repo/traceMethods', 'GET', null, false);
    // alert('Response updateTraceMethodOptions: ' + JSON.stringify(response));

    traceMethods = response.body.trace_methods;
    traceMethods.forEach(option => {
        const button = document.createElement('button');
        button.type = 'button';
        button.classList.add('btn', 'btn-outline-primary', 'btn-group-trace-methods');
        button.textContent = option;
        button.addEventListener('click', function () {
            // Toggle the active class and update the hidden input
            const allButtons = document.getElementsByClassName('btn-group-trace-methods');
            for (const otherButton of allButtons) {
                otherButton.classList.remove('active');
            }
            button.classList.toggle('active');
            const selectedTraceMethodInput = document.getElementById('selectedTraceMethod');
            selectedTraceMethodInput.value = button.classList.contains('active') ? option : '';
        });
        traceMethodButtons.appendChild(button);
    });
}

// Function to synchronize slider value with floating number input
function syncSliderValue(slider, input) {
    const floatInput = document.getElementById('floatInput');
    const sliderInput = document.getElementById('sliderInput');
    const selectedThreshold = document.getElementById('selectedThreshold');

    floatInput.addEventListener('input', updateSlider);
    sliderInput.addEventListener('input', updateFloatInput);

    function updateSlider() {
        sliderInput.value = floatInput.value;
        selectedThreshold.value = floatInput.value;
    }

    function updateFloatInput() {
        floatInput.value = sliderInput.value;
        selectedThreshold.value = sliderInput.value;
    }
}

// Function to delete all trace links
async function deleteTraceLinks(){
    var selectedRepo = localStorage.getItem('selected_repo');
    if (!selectedRepo) {
        alert('No repo selected');
        return;
    }
    const uri = 'http://localhost:3000/api/repo/' + selectedRepo + '/trace';
    const response = await makeApiRequest(uri, 'DELETE', null, false);
    if (response.status != 200) {
        console.log('ResponseDeleteTraceLinks: ' + JSON.stringify(response) + response.status);
        return;
    }
    alert('Trace links deleted.');
}

// ----------------------------------------

// Function to update repository values section
async function updateRepoDetailsSection() {
    var selectedRepo = localStorage.getItem('selected_repo');
    if (!selectedRepo) {
        alert('No repo selected');
        return;
    }
    const repoValues = await getRepoDetails();

    const repoValuesSection = document.getElementById('repoDetailsSection');
    // Clear existing data
    repoValuesSection.innerHTML = '';
    const repo_name = document.createElement('p');
    repo_name.textContent = 'Name: ' + selectedRepo.split('.')[0] + '/' + selectedRepo.split('.')[1];
    repoValuesSection.appendChild(repo_name);
    // for each data in repoValues, add a new paragraph
    for (const [key, value] of Object.entries(repoValues)) {
        const paragraph = document.createElement('p');
        paragraph.textContent = key + ': ' + value;
        repoValuesSection.appendChild(paragraph);
    }
    repoValuesSection.innerHTML = repoValuesHTML;
}

// Function to get repository values
async function getRepoDetails() {
    // Replace this with actual logic to fetch repository values
    var selectedRepo = localStorage.getItem('selected_repo');
    const uri = 'http://localhost:3000/api/repo/' + selectedRepo;
    const response = await makeApiRequest(uri, 'GET', null, false);
    if (response.status != 200) {
        console.log('ResponseGetRepoDetails: ' + JSON.stringify(response) + response.status);
        return;
    }
    console.log(response.body);
    return response.body;
}