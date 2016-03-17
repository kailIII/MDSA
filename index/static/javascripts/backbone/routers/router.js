var SistemasRouter = Backbone.Router.extend({
	
	routes: {
		'usuario/'			  : 'usuario_menu',  
		'usuario/create/'	  : 'usuario_create',  
		'usuario/detail/:pk/' : 'usuario_detail',  
	},
	initialize:function(){
		Backbone.history.start({pushState: true});
	},
	usuario_menu: function() {

		var botonMenuOpen = new Sistemas.Models.BotonMenuOpen();
		var botonMenuClose = new Sistemas.Models.BotonMenuClose();
		var menu1 = new Sistemas.Models.MenuGrafico({ nombre:'Nuevo Usuario', URL:'usuario:creador'});
		var menu2 = new Sistemas.Models.MenuGrafico({ nombre:'Consultar', URL:'detail'});
		var menu3 = new Sistemas.Models.MenuGrafico({ nombre:'Reporte', URL:'#create'});
		
		var modulo1 = new Sistemas.Models.MenuModulo({ nombre:'Trámite Documentario'});
		var modulo2 = new Sistemas.Models.MenuModulo({ nombre:'Control de Asistencia'});
		var modulo3 = new Sistemas.Models.MenuModulo({ nombre:'Caja'});
		
		var list_menu = new Sistemas.Collections.MenuGrafico([menu1, menu2, menu3]);
		var list_modulo = new Sistemas.Collections.MenuModulo([modulo1, modulo2, modulo3]);

		var menus = new Sistemas.Views.MenusGraficos({collection:list_menu});
		var modulos = new Sistemas.Views.MenusModulos({collection:list_modulo});
		
		var botonOpenView = new Sistemas.Views.BotonMenuOpen({model:botonMenuOpen});
		var botonCloseView = new Sistemas.Views.BotonMenuClose({model:botonMenuClose});

		botonOpenView.render();
		menus.render();
		botonCloseView.render();
		modulos.render();
	},
	usuario_create:function(){
		alert("create");
	},
	usuario_detail:function(pk){
		alert("hola" + pk);
	}

});

Sistemas.Routers.SistemasRouter = SistemasRouter;