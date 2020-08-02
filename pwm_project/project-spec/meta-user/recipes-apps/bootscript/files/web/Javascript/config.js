function rest_call(uri, callback, complete_callback)
{
    $.ajax({
        url: uri,
        success: callback,
        complete: complete_callback,
        error: function(xhr, error_status, error_thrown)
        {
            console.log(error_status);
        }
    });
}

function recovery_mode()
{
    alert("The unit is going to reboot in firmware update mode");
    $("#restart_panel").show();

    var url = '/cgi-bin/recovery_mode'

    rest_call(url, function(data) {
        console.log(data);

        if (data.Error != 0)
        {
            alert('Unable to restart');
        }

        setTimeout(function()
        {
            console.log('Restarting client')
            window.location.reload(); 
            window.location.href = '/';
        }, 20000);
    });
}

function load_configuration()
{
    var url = '/cgi-bin/fw_revision';
    rest_call(url, function(data) {
        console.log(data);

        for (var configuration_item in data)
        {
            var element = $('#' + configuration_item);

            $(element).text(data[configuration_item]);
        }
    });
}

function form_rgb_str(red_c, green_c, blue_c)
{
    return "rgb(" + (red_c * 5) + ", " + (green_c * 5) + ", " + (blue_c * 5) + ")";
}

function set_led(register_name, value)
{
    var url = '/cgi-bin/rgb-led-pwm?register=' + register_name + '&value=0x' + (+value).toString(16);

    rest_call(url, function(data) {
        console.log(data);
 
        if (data.Error != 0)
        {
            alert('Unable to set register value');
        }
    });
}

function save_IP()
{
    var userIP = document.getElementById("net_ip_address").value;
    alert("IP Changed:" + userIP);
    console.log(userIP);
    $.ajax({
        type: "GET",
        url: '/cgi-bin/GUI',
        data: userIP,
        success:function(data){
            console.log(data);
            }
        });
}
