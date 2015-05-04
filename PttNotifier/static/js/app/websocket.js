(function(global){
    var wsurl = 'ws://buzz3.co';
    var socket = io.connect(wsurl);

    socket.on('date', function(data) {
        $('#wstest').text(data.date);
    });

    socket.on('notify', function(data) {
        console.log('count: ' + data.count);
        localStorage.setItem('buzz3push', data.count);
        $('.notifications-dropdown-container').text(data.count);
    });

    var resetNotifications = function(content){
        var targetDiv = $('#notifications-binding');
        targetDiv.empty();
        var data = JSON.parse(content)
        console.log(data);
        var htmlContent = '';
        var counter = 0;
        for(var key in data) {
            // htmlContent +=
            //     '<a class="notification-content-block" href="' + key + '" target="_blank"> \
            //         <div class="notification-item"> \
            //             <h4 class="item-title">' + data[key] + '</h4> \
            //             <p class="item-info">' + key + '</p> \
            //         </div> \
            //     </a>';
            htmlContent += '<li><a class="notification-item" href"' + key + '" target="_blank">' + data[key] + '</a></li>';
            if (counter >= 5) {
                htmlContent += '<li class="divider"></li> \
                    <li><a href="#!" class="notification-item">More</a></li>';
                    break;
            }
        }
        targetDiv.append(htmlContent);
    };
    //<ul id="dropdown1" class="dropdown-content">
    //    <li><a href="#!" id="dropdown_content_1" class="dropdown_content">one</a></li>
    //    <li><a href="#!" id="dropdown_content_2" class="dropdown_content">two</a></li>
    //    <li class="divider"></li>
    //    <li><a href="#!" id="dropdown_content_3" class="dropdown_content">three</a></li>
    //  </ul>


    $('#notification-li').click(function(){
        ajaxGet('/rtnotifications/', function(content){
            resetNotifications(content);
        });
    });
    $('.notification-content-block').click(function(){
        var url = $(this).find('.item-title').text;
        var title = $(this).find('.item-info').text;
        var postBody = { 'url': url, 'title': title }
        ajaxPost('/rtnotifications/update', postBody, function(content){
            resetNotifications(content);
        });
    });


})(this);