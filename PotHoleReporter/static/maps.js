var map;
    centerMap = [
        //Buffalo
        [42.880230, -78.878738],
        //Amherst
        [42.979111, -78.799263],
        //Clarence
        [42.980968, -78.587250],
        //West Seneca
        [42.839570, -78.753841],
        //Cheektowaga
        [42.906281, -78.754341],
        //Tonawanda
        [43.021816, -78.878783],
        //Eden
        [42.652410, -78.896940],
        //Grand Island
        [43.036430, -78.962692],
        //Lancaster
        [42.892780, -78.676422],
        //Williamsville
        [42.963169, -78.742912],
        //Hamburg
        [42.720128, -78.827987],
        //Orchard Park
        [42.767460, -78.743912],
        //Depew
        [42.901810, -78.695000],
        //Kenmore
        [42.962818, -78.870041],
        //Angola
        [42.638460, -79.027690]
    ];
    function initMap() {
            console.log(centerMap[town-1]);
            map = new google.maps.Map(document.getElementById('map'), {
            zoom: 14,
            center: new google.maps.LatLng(centerMap[town-1][0], centerMap[town-1][1]),
            mapTypeId: 'roadmap'
            });

    var potLocations = 'http://pothole.us-east-1.elasticbeanstalk.com/locations/' + town;
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
            description: obj.locations[i].description,
            };
    locations.push(myAdd);
    }
    locations.forEach(function(feature) {
            console.log(feature);
            var contentString = "<h5> Ticket #"+ feature.title +"</h5>"+
                "<p><b>Size:</b> "+ feature.size + "</p>"+
                "<p><b>Description:</b> "+ feature.description + "</p>";;
            
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