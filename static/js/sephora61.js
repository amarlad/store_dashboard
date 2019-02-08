var iconBase = 'https://maps.google.com/mapfiles/kml/shapes/';
var iconBase1 = '../static/images/';
var icons = {
   store: {
     icon: iconBase1 + 'sephora.png'
   },
   parking: {
     icon: iconBase + 'parking_lot_maps.png'
   },
   library: {
     icon: iconBase + 'library_maps.png'
   },
   info: {
     icon: iconBase + 'info-i_maps.png'
   }
};

// Create markers.
function addMarker(location) {
  var marker = new google.maps.Marker({
     position: location,
     icon: icons['info'].icon,
     map: map
  });
};

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
      zoom: 5,
      center: new google.maps.LatLng(39, -95),
      mapTypeId: 'roadmap'
    });

    for (var i = 0; i < jsonReader['location'].length; i++) {
      var latlang = jsonReader['location'][i];
      var storeLocation = new google.maps.LatLng(latlang['latitude'], latlang['longitude']);
      addMarker(storeLocation);
    };
}


  // var lat = jsonReader['location'][1]['latitude'];
  // alert(lat);  

//     for (var i = 0; i < jsonReader['location'].length; i++) {
//       var latlang = jsonReader['location'][i];
// //    alert(latlang['latitude'] + ' ' + latlang['longitude'])


  

//   var features = [
//     {
//       position: new google.maps.LatLng(35.0932882679133, -89.8115834028014),
//       type: 'store'
//     }, {
//       position: new google.maps.LatLng(37.698166752093, -121.928298546045),
//       type: 'info'      
//     },{
//       position: new google.maps.LatLng(21.3333666, -158.0517197),
//       type: 'info'
//     }
//   ];


// }