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
  layers:'geonode:lim_bairro_a',
  transparent: 'true',
  format: 'image/png'
  });

  //CONTROLE DE CAMADAS

	var basecarto = {
		"OpenStreetMap": osm,
		"GoogleSatelite": imagemSat,
  };

	var feicoes = {
    //"Pontos de Coleta": pontos_coleta,
    "Lotes": lotes,
		"Divisas de Bairro": divisadebairros,
    "Ocupacoes Irregulares": OcupacoesIrreg,
    "Hidrografia Linha": hidrografiaL,
	};

	//Adicionar objetos ao controle de camadas
	L.control.layers(basecarto, feicoes).addTo(map);


  //GRADES DE COORDENADAS
  // Specify divisions every 0.5 degrees
  // L.graticule({ interval: 0.05 }).addTo(map);
  // L.graticule({
  //   style: {
  //       color: '#f00',
  //       weight: 1,
  //   }
  // }).addTo(map);


 }
