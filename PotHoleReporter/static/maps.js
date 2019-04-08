var map;
    function initMap() {
            map = new google.maps.Map(document.getElementById('map'), {
            zoom: 16,
            center: new google.maps.LatLng(42.880230, -78.878738),
            mapTypeId: 'roadmap'
            });

    var potLocations = 'http://127.0.0.1:5000/locations';
    var locations = [];
    fetch(potLocations)
    .then(function(response) {
    return response.text();
    }).then(function(body) {
    var obj = JSON.parse(body);
    var myAdd = {};
    var addresses = obj.cordinates;
    var l = addresses.length;
    for (i = 0; i < l; i++) {
    myAdd = {
        position: {
            lat: parseFloat(obj.cordinates[i].lat),
            lng: parseFloat(obj.cordinates[i].lng)
                    },
            title: obj.cordinates[i].title,
            };
    locations.push(myAdd);
    }
    locations.forEach(function(feature) {
            var marker = new google.maps.Marker({
                position: feature.position,
                map: map,
                title: feature.title
            });
            });

    }).catch(function() {
    // if the ajax call fails display an error in an info window
                    var pos = {
                        lat: lat,
                        lng: lng
                    };
                    infoWindow.setMap(map);
                    infoWindow.setPosition(pos);
                    infoWindow.setContent('An error occurred, we are unable to retreive cordinates.');

                });
    }