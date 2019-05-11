
/* Load the gapi.client library */
function start() {
    gapi.load('auth2', function() {
            auth2 = gapi.auth2.init({
            client_id: '1064370308162-tckief3fggm0aa3ge58ajsdm8i7qdgt8.apps.googleusercontent.com'
        });
    });
}

/* Process authentication result */
function logInCallback(authResult) {
    if (authResult['code']) {
        let $gLoginButton = $('#gLoginButton');
        $gLoginButton.attr('style', 'display: none');

        let state = $gLoginButton.data('state');

        $.ajax({
            type: 'POST',
            url: '/glogin?state=' + state,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            },
            contentType: 'application/octet-stream; charset=utf-8',
            success: function(result) {
                if (result) {
                    $('#result').html('Login Successful!<br><br>'+ result + '<br>Redirecting...');

                    setTimeout(function() {
                        window.location.href = "/";
                    }, 2000);
                } else if (authResult['error']) {
                    displayMessage('User authorization failed.');
                    console.log('There was an error: ' + authResult['error']);
                } else {
                    displayMessage('Failed to make a server-side call.');
                }
            },
            error: function(jqXHR, textStatus, errorThrown) {
                displayMessage('Authorization request failed: ' + errorThrown);
            },
            processData:false,
            data: authResult['code']
        });
    } else {
        // handle error
        displayMessage('Failed to make a server-side call. Check sign in configuration and console.');
    }
}

/* Log Google account user out */
function logout() {
    $('#logout-info').hide();

    $.ajax({
        type: 'GET',
        url: '/glogout',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        },
        contentType: 'application/octet-stream; charset=utf-8',
        success: function(result) {
            if (result) {
                displayMessage(result + '<br><br>Redirecting...');

                setTimeout(function() {
                    window.location.href = "/";
                }, 2000);
            } else if (authResult['error']) {
                displayMessage('User logout failed.');
                console.log('There was an error: ' + authResult['error']);
            } else {
                displayMessage('Failed to make a server-side call.');
            }
        },
        error: function(jqXHR, textStatus, errorThrown) {
            displayMessage('Log out request failed: ' + errorThrown);
        }
    });
}

/* Display messages and erros */
function displayMessage(message) {
    $('#message').html(message);
    $('#login-back').css('display', 'inline-block');
}

/* Bind button events */
$(document).ready(function() {
    let $gLoginButton = $('#gLoginButton');
    let $gLogoutButton = $('#gLogoutButton');

    if ($gLoginButton.length > 0) {
        $gLoginButton.click(function() {
            auth2.grantOfflineAccess().then(logInCallback);
        });
    }

    if ($gLogoutButton.length > 0) {
        $gLogoutButton.show();
        $gLogoutButton.click(logout);
    }
});