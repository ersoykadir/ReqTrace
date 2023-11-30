async function makeApiRequest(apiUrl, selectedMethod, body, form) {

    // Get the access token from localStorage
    var accessToken = localStorage.getItem('access_token');
    
    if (!accessToken) {
        alert('No access token found in localStorage. Please Login first.');
        return;
    }
    var headers = new Headers();
    headers.append('Authorization', 'Bearer ' + accessToken);

    // Make the API request using the selected HTTP method
    // contentType = 'application/json';
    // if (form) {
    //     contentType = 'multipart/form-data';
    // }
    var info = {
        method: selectedMethod,
        headers: headers,
    };
    if (selectedMethod == 'POST') {
        if (form) {
            info = {
                method: 'POST',
                headers: headers,
                body: body,
            };
        }
        else {
            headers.append('Content-Type', 'application/json');
            info = {
                method: 'POST',
                headers: headers,
                body: JSON.stringify(body),
            };
        }
    }
    // info = JSON.stringify(info);
    try {
        const response = await fetch(apiUrl, info);
        return {
            status: response.status,
            body: await response.json()
        }
    } catch (error) {
        console.error("Error: ", error);
        throw error;
    }
}

async function createTraceLinks(event){
    event.preventDefault();
    var selectedRepo = localStorage.getItem('selected_repo');
    var selectedSourceArtifact = document.getElementById('sourceSelectedArtifact').value;
    var selectedTargetArtifact = document.getElementById('targetSelectedArtifact').value;
    var selectedTraceMethod = document.getElementById('selectedTraceMethod').value;
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
    console.log( selectedSourceArtifact + ' ' + selectedTargetArtifact + ' ' + selectedTraceMethod )
    var body = {
        'source_artifact_type': selectedSourceArtifact,
        'target_artifact_type': selectedTargetArtifact,
        'trace_method': selectedTraceMethod
    };
    // body = JSON.stringify(body);
    const response = await makeApiRequest(uri, 'POST', body, false);
    if (response.status != 200) {
        alert('ResponseCreateTraceLinks: ' + JSON.stringify(response) + response.status);
        return;
    }
    alert('Trace links created.');
}

async function populateRepo(event) {
    event.preventDefault(); // Prevent the default form submission behavior
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

    const response = await makeApiRequest(uri, 'POST', formData, true);
    updateArtifactOptions('source');
    updateArtifactOptions('target');
    if (response.status != 200) {
        alert('ResponsePopulateRepo: ' + JSON.stringify(response) + response.status);
        return;
    }
    alert('Repo populated.');
}

// async function populateRepo(event) {
//     event.preventDefault();

//     var selectedRepo = localStorage.getItem('selected_repo');
//     const uri = 'http://localhost:3000/api/repo/' + selectedRepo + '/populate';
//     // Set the action attribute of the form dynamically
//     var customForm = document.getElementById('populateRepoForm');
//     customForm.action = uri; // Replace with your desired action URL
//     // Submit the form
//     customForm.submit();
// }

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
        var repoHeader = document.getElementById('repoHeader');
        repo_owner = selectedRepo.split('.')[0];
        repo_name = selectedRepo.split('.')[1];
        repoHeader.innerHTML = 'Repository: ' + repo_owner + '/' + repo_name;
    } else {
        // No repository method selected, you can handle this case accordingly
        console.warn('No Repository Selected');
    }
}

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

// Function to update the trace method buttons
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

// Function to update the trace method buttons
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
    body = JSON.parse(JSON.stringify(body));
    const response = await makeApiRequest('http://localhost:3000/api/repo', 'POST', body, false);
    if (response.status != 200) {
        alert('ResponseCreateRepoForm: ' + JSON.stringify(response) + response.status);
    }
    else {
        // alert('ResponseCreateRepoForm: ' + JSON.stringify(response) + response.status);
        await updateRepoOptions();
    }
}

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
// processAccessToken();

// Initial update of repository options when the page loads
// updateRepoOptions();
// updateArtifactsOptions();
// updateTraceMethodOptions();

// window.onload = onPageLoad;

async function redirectToPage(page) {
    // window.location = page;
    window.open(page, '_newtab');
}