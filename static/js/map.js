window.onload = init;

function init(){
    const mymap = L.map(mapid, {
        center: [1.5057479240587752, 103.78105169353988],
        zoom: 14,
        layers: [
            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
})
        ]
        // layers: [
        //     L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
        //         attribution:  '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy;'
        //     })
        // ]
    })
    
}
