document.addEventListener('DOMContentLoaded', init)

function init(){
    // Leaflet Map
    const map = L.map('map').setView([1.503498, 103.788742], 14)
    L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
            attribution:  '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy;'
        }).addTo(map)

        // Fetch API - Get Request
        const fetchGetRequest = async(url, func) => {
            try {
                const response = await fetch(url)
                const json = await response.json()
                return func(json)
            } catch (error) {
                console.log(error.message)
            }
        }

        const pointStyle = {
            stroke: true,
            radius: 11,
            color: 'black',
            weight: 2,
            opacity: 1,
            fillColor: 'green',
            fillOpacity: 1,
        }

        const selectedPointStyle = {
            stroke: true,
            radius: 11,
            color: 'red',
            weight: 2,
            opacity: 1,
            fillColor: 'white',
            fillOpacity: 1,
        }

        const styleGeoJSONOnClick = (places) => {
            let lastClickedFeature;

            places.on('click', (e) => {
                if (lastClickedFeature){
                    places.resetStyle(lastClickedFeature)
                }

                lastClickedFeature = e.layer;
                e.layer.setStyle(selectedPointStyle)
            })
        }

        // Add three nearest city
        // var nearbyCitiesGeoJSONLayer;
        // const addNearbyCities = (geojson) => {
        //     if (nearbyCitiesGeoJSONLayer) {
        //         map.removeLayer(nearbyCitiesGeoJSONLayer)
        //     }
        //     nearbyCitiesGeoJSONLayer = L.GeoJSON(geojson, {}).addTo(map)
        // }

        // addNearbyCitiesLogic
        // const addNearbyCitiesLogic = (id) => {
        //     let url = "/api/v1/cities/?placeid="+ id;
        //     fetchGetRequest(url, addNearbyCities);
        // }

        const placeImageElement = document.getElementById('placeImage');
        const menuTitleElement = document.getElementById('menu-title');
        const menuTextElement = document.getElementById('menu-text');

        // GeoJSON popup and menu informationp
        const onEachFeatureHandler = (feature, layer) => {
            // Popup for feature - on click display feature name
            let placeName = feature.properties.place_name
            layer.bindPopup("<center>Nama Projek: " + "<br><b>" +  placeName + "</b></center>")

            // no image available source
            let noImageAvailable = './media/place_images/no-image-placeholder.png';

            // On click, update menu information
            layer.on('click', (e) => {
                let featureImage = feature.properties.image ? feature.properties.image: noImageAvailable
                let featureDescription = feature.properties.description

                menuTitleElement.innerHTML = "<center>Nama Projek: " + "<br><b>" +  placeName + "</b></center>";
                placeImageElement.setAttribute('src', featureImage);
                menuTextElement.innerHTML = featureDescription;

                // let featureID = feature.properties.pk;
                // addNearbyCitiesLogic(featureID)
            })
        }

        // GeoJSON Layer
        const addAllPlacesToMap = (json) => {
            let places = L.geoJSON(json, {
                // Change default marker to circle marker
                pointToLayer: function(feature, latlng){
                    return L.circleMarker(latlng, pointStyle)
                },
                onEachFeature: (feature, layer) => {
                    onEachFeatureHandler(feature, layer)
                }
            }).addTo(map)

            // Style GeoJSON Click
            styleGeoJSONOnClick(places)

        }

        fetchGetRequest('/api/v1/places/', addAllPlacesToMap)
    }
