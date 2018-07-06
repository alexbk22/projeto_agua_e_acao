// window.onload = function() {
//
//   //1 - Mapa centrado em Curitiba
// 	var mapa = L.map("meumapa", {
// 		center: [-25.45, -49.25],
// 		zoom: 5,
// 		zoomSnap: 0.5,
// 		zoomDelta: 0.5,
// 		minZoom: 4.5,
// 		maxZoom: 11
// 	});
//
// 	// funçao para adicionar o geodjson ao mapa
//   function add_geojson (f){
//
//   var geojsonMarkerOptions = {
//     radius: 8,
//     fillColor: "#ff7800",
//     color: "#000",
//     weight: 1,
//     opacity: 1,
//     fillOpacity: 0.8
// };
//
//     var geo = f;
// 		var layer_geojson = L.geoJson();
//     layer_geojson.clearLayers();
//
//     layer_geojson = L.geoJSON(geo, {
// 		style: geojsonMarkerOptions
// 	}).addTo(mapa);
//    mapa.fitBounds(layer_geojson.getBounds());
// };
//
// //var mapa = L.map("meumapa").setView([-25.5, -49.25], 11);
// //var osm = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(mapa);
// //2 - Camadas base
//
//   var osmColorido = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(mapa);
//
// 	// funcao ajax para enviar parametros pro python e retornar geojson
// 	function Consulta_tema_data() {
//
// 			var regiao='sul';
// 	    //var basicValues = $("#slider").dateRangeSlider("values");
// 	    //var opcao= document.getElementById("tema").value;
// 	   // var data_inicial = trans_data(basicValues.min);
// 	    //var data_final = trans_data(basicValues.max);
//
// 	    //$.get('consulta', {consulta_tema: opcao, d_i:data_inicial, d_f:data_final }, function(data){
// 			$.get('consulta', {consulta_tema: regiao}, function(data){
// 				console.log (data);
// 	      add_geojson(data);
// 	    }
// 	  )
// 	}
// }
//1 - Mapa centrado em Curitiba
var mapa = L.map("mapa_consulta", {
	center: [-25.45, -49.25],
	zoom: 5,
	zoomSnap: 0.5,
	zoomDelta: 0.5,
	minZoom: 4.5,
	maxZoom: 11
});

//2 - Camadas base
var osmColorido = L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(mapa);

// funcao ajax para enviar parametros pro python e retornar geojson
function Consulta_Ponto() {

		var regiao='P8';

		//$.get('consulta', {consulta_tema: opcao, d_i:data_inicial, d_f:data_final }, function(data){
		$.get('consulta', {consulta_tema: regiao}, function(data){
		 add_geojson(data);
	 }
	)
};

function add_geojson (f){

		var geojsonMarkerOptions = {
		radius: 8,
		fillColor: "#ff7800",
		color: "#000",
		weight: 1,
		opacity: 1,
		fillOpacity: 0.8
}

		var geo = f;
		var layer_geojson = L.geoJson();
		layer_geojson.clearLayers();

		layer_geojson = L.geoJSON(geo, {

		style: function (feature) {
			return feature.properties && feature.properties.style;
		},
		onEachFeature: function (feicao, camada){
				camada.bindTooltip(feicao.properties.pt_id)
				return L.circleMarker(camada, geojsonMarkerOptions)},

		pointToLayer: function (feature, latlng) {

			return L.circleMarker(latlng, {
			radius: 4,
				fillColor: "#ff7800",
				color: "#000",
				weight: 1,
				opacity: 1,
				fillOpacity: 0.8
			});
		}
	}).addTo(mapa);
	 mapa.fitBounds(layer_geojson.getBounds());
};
