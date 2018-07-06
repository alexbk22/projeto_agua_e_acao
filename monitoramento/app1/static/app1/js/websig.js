//1 - Mapa centrado no Centro Politecnico
var map

window.onload = function() {


    map = L.map("websig", {


		measureControl:true,
		center: [-25.4505, -49.2370],
		zoom: 16,

		zoomSnap: 0.5,
		zoomDelta: 0.5,
		minZoom: 0,
		maxZoom: 18
	});

  //BARRA DE ESCALA
  L.control.betterscale({metric:true, imperial:false}).addTo(map);


  //BARRA FERRAMENTAS
  var barraferramentas = L.control.navbar({
                position: "topleft"
                }).addTo(map);


  //COLETA DE COORDENADAS
  var c = new L.Control.Coordinates();

  c.addTo(map);

  map.on('click', function(e) {
  c.setCoordinates(e);
  });


  //CAMADAS BASE

  var osm = L.tileLayer('https://{s}.tile.openstreetmap.de/tiles/osmde/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  });

  var imagemSat = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
  }).addTo(map);

  //Adicionando um mini mapa
	var CartoDB_Positron_2 = L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}.png', {
 	attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a> &copy; <a href="http://cartodb.com/attributions">CartoDB</a>',
 	subdomains: 'abcd',
 	maxZoom: 19
  });
	var miniMap = new L.Control.MiniMap(CartoDB_Positron_2).addTo(map);

  //4 - Adicionando o WMS
  var OcupacoesIrreg = L.tileLayer.wms('http://www.idea.ufpr.br/geoserver/geonode/wms', {
  layers:'geonode:ocupacao_irregular',
  transparent: 'true',
  format: 'image/png'
  }).addTo(map);

  var lotes = L.tileLayer.wms('http://www.idea.ufpr.br/geoserver/geonode/wms', {
  layers:'geonode:lotes_wgs84',
  transparent: 'true',
  format: 'image/png'
  });

  var hidrografiaL = L.tileLayer.wms('http://www.idea.ufpr.br/geoserver/geonode/wms', {
  layers:'geonode:hidrol',
  transparent: 'true',
  format: 'image/png'
  });

  var divisadebairros = L.tileLayer.wms('http://www.idea.ufpr.br/geoserver/geonode/wms', {
  layers:'geonode:bairro_cwb_sirgas',
  transparent: 'true',
  format: 'image/png'
  });

  //CONTROLE DE CAMADAS

	var basecarto = {
		"OpenStreetMap": osm,
		"GoogleSatelite": imagemSat,
  };

	var feicoes = {
    "Lotes": lotes,
		"Divisas de Bairro": divisadebairros,
    "Ocupacoes Irregulares": OcupacoesIrreg,
    "Hidrografia 1/25000": hidrografiaL,
	};

	//Adicionar objetos ao controle de camadas
	L.control.layers(basecarto, feicoes).addTo(map);

};

 //funcao para ocultar e mostrar formulario
 function Mudarestado(el){
  var display = document.getElementById(el).style.display;
  if(display == "none")
    document.getElementById(el).style.display = 'block';
  else
    document.getElementById(el).style.display = 'none';
};

//###### alex mexendo
// funcao ajax para enviar parametros pro python e retornar geojson
function Consulta_Ponto(P) {
    if (P=='todos_pts'){
      $.get('consultajson1', function(data){
        add_geojson(data);
        }
      )
    }

    if (P=='nome_pt'){
      var nome = prompt("Digite o nome do ponto: ");
      $.get('consultanome', {consulta_nome: nome}, function(data){
        }
      )
    }

    /*if (P=='consult2'){
      var nome_do_ponto='P2';
      //$.get('consulta', {consulta_tema: opcao, d_i:data_inicial, d_f:data_final }, function(data){
      $.get('consultajson2', {consulta_tema: nome_do_ponto}, function(data){
        add_geojson(data);
        }
      )
    }*/

};
// funcao ajax para enviar parametros pro python e retornar geojson
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
  }).addTo(map);
   map.fitBounds(layer_geojson.getBounds());
};


// // funcao para popular um dropdown
// function nome_pts(o){
//   var $seletor = $("#tema");
//   $.each(o, function() {
//       $seletor.append($("<option />").val(this).text(this));
//     }
//   );
// }
