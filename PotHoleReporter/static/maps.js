var map;
    function initMap() {
            map = new google.maps.Map(document.getElementById('map'), {
            zoom: 16,
            center: new google.maps.LatLng(42.880230, -78.878738),
            mapTypeId: 'roadmap'
            });

    var potLocations = 'http://pothole.us-east-1.elasticbeanstalk/locations/' + town;
    var locations = [];
    fetch(potLocations)
    .then(function(response) {
    return response.text();
    }).then(function(body) {
    var obj = JSON.parse(body);
    var myAdd = {};
    
    var addresses = obj.locations;
    var l = addresses.length;
    for (i = 0; i < l; i++) {
    myAdd = {
        position: {
            lat: parseFloat(obj.locations[i].lat),
            lng: parseFloat(obj.locations[i].lng)
                    },
            title: obj.locations[i].title,
            size: obj.locations[i].size,
            };
    locations.push(myAdd);
    }
    locations.forEach(function(feature) {
            var contentString = "<h5> Ticket #"+ feature.title +"</h5>"+
                "<p><b>Size:</b> "+ feature.size + "</p>";
            
            var infowindow = new google.maps.InfoWindow({
                    content: contentString
            });

            var marker = new google.maps.Marker({
                position: feature.position,
                map: map,
                title: feature.title
            });
            marker.addListener('click', function() {
                infowindow.open(map, marker);
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