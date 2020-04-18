if(window.matchMedia("(min-width:700px)").matches){
    var map = new naver.maps.Map('map', {
        center: new naver.maps.LatLng(35.889388, 128.610293),
        zoom: 16
    });

    var polygon1 = new naver.maps.Polygon({
        map: map,
        paths: [
            [
                new naver.maps.LatLng(35.892015, 128.608700),
                new naver.maps.LatLng(35.886681, 128.604936),
                new naver.maps.LatLng(35.885647, 128.615360)
            ]
        ],
        fillColor: 'red',
        fillOpacity: 0.3,
        strokeColor: 'red',
        strokeOpacity: 0.6,
        strokeWeight: 3,
        clickable: true
    });

     var infoWindow1 = new naver.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:10px;font-size:16px;">고양이1 출몰지역</div>'
    });

    var coord1 = new naver.maps.LatLng(35.888011, 128.608556);

    naver.maps.Event.addListener(polygon1,"mouseover", function() {

        polygon1.setOptions({
            strokeColor: 'red',
            strokeOpacity: 1
        });
        infoWindow1.open(map,coord1);
    });

    naver.maps.Event.addListener(polygon1, "mouseout", function() {

        polygon1.setOptions({
            strokeColor: 'red',
            strokeOpacity: 0.6
        });
        infoWindow1.close();
    });


    var polygon2 = new naver.maps.Polygon({
        map: map,
        paths: [
            [
                new naver.maps.LatLng(35.885647, 128.615360),
                new naver.maps.LatLng(35.892015, 128.608700),
                new naver.maps.LatLng(35.895725, 128.613510)
            ]
        ],
        fillColor: '#ffff00',
        fillOpacity: 0.3,
        strokeColor: 'red',
        strokeOpacity: 0.6,
        strokeWeight: 3,
        clickable: true
    });

     var infoWindow2 = new naver.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:10px;font-size:16px;">고양이2 출몰지역</div>'
    });

    var coord2 = new naver.maps.LatLng(35.891215, 128.612071);


    naver.maps.Event.addListener(polygon2,"mouseover", function() {

        polygon2.setOptions({
            strokeColor: 'red',
            strokeOpacity: 1
        });
        infoWindow2.open(map,coord2);
    });

    naver.maps.Event.addListener(polygon2, "mouseout", function() {

        polygon2.setOptions({
            strokeColor: 'red',
            strokeOpacity: 0.6
        });
        infoWindow2.close();
    });
}
else{
    var map = new naver.maps.Map('map', {
        center: new naver.maps.LatLng(35.888466, 128.610336),
        zoom: 15
    });

    var polygon1 = new naver.maps.Polygon({
        map: map,
        paths: [
            [
                new naver.maps.LatLng(35.892015, 128.608700),
                new naver.maps.LatLng(35.886681, 128.604936),
                new naver.maps.LatLng(35.885647, 128.615360)
            ]
        ],
        fillColor: 'red',
        fillOpacity: 0.3,
        strokeColor: 'red',
        strokeOpacity: 0.6,
        strokeWeight: 3,
        clickable: true
    });

     var infoWindow1 = new naver.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:10px;font-size:16px;">고양이1 출몰지역</div>'
    });

    var coord1 = new naver.maps.LatLng(35.888011, 128.608556);

    naver.maps.Event.addListener(polygon1,"mouseover", function() {

        polygon1.setOptions({
            strokeColor: 'red',
            strokeOpacity: 1
        });
        infoWindow1.open(map,coord1);
    });

    naver.maps.Event.addListener(polygon1, "mouseout", function() {

        polygon1.setOptions({
            strokeColor: 'red',
            strokeOpacity: 0.6
        });
        infoWindow1.close();
    });


    var polygon2 = new naver.maps.Polygon({
        map: map,
        paths: [
            [
                new naver.maps.LatLng(35.885647, 128.615360),
                new naver.maps.LatLng(35.892015, 128.608700),
                new naver.maps.LatLng(35.895725, 128.613510)
            ]
        ],
        fillColor: '#ffff00',
        fillOpacity: 0.3,
        strokeColor: 'red',
        strokeOpacity: 0.6,
        strokeWeight: 3,
        clickable: true
    });

     var infoWindow2 = new naver.maps.InfoWindow({
            content: '<div style="width:150px;text-align:center;padding:10px;font-size:16px;">고양이2 출몰지역</div>'
    });

    var coord2 = new naver.maps.LatLng(35.891215, 128.612071);


    naver.maps.Event.addListener(polygon2,"mouseover", function() {

        polygon2.setOptions({
            strokeColor: 'red',
            strokeOpacity: 1
        });
        infoWindow2.open(map,coord2);
    });

    naver.maps.Event.addListener(polygon2, "mouseout", function() {

        polygon2.setOptions({
            strokeColor: 'red',
            strokeOpacity: 0.6
        });
        infoWindow2.close();
    });
}