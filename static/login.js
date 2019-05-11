
function start() {
    gapi.load('auth2', function() {
            auth2 = gapi.auth2.init({
            client_id: '1064370308162-tckief3fggm0aa3ge58ajsdm8i7qdgt8.apps.googleusercontent.com'
        });
    });
}

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
                    console.log('There was an error: ' + authResult['error']);
                } else {
                    $('#result').html('Failed to make a server-side call. Check your configuration and console.');
                }
            },
            processData:false,
            data:authResult['code']
        });
    } else {
        // handle error
        $('#result').html('Failed to make a server-side call. Check your configuration and console.');
    }
}

$(document).ready(function() {
    $('#gLoginButton').click(function() {
        auth2.grantOfflineAccess().then(logInCallback);
    });
});