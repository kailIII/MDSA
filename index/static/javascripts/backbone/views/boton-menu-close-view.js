var BotonMenuClose = Backbone.View.extend({
	tagName   : 'a',
	className : 'MenuHeadModulo-Boton-Link', 
	el 		  : $('#Menu-Boton-Close'),
	//template  : Handlebars.compile($('#BotonMenu-Close-Template').html()),
	template  : _.template($('#BotonMenu-Close-Template').html()),
	events : {
		'click #Menu-Close' : 'closeMenu',
	},

	closeMenu:function (e) {
	 	e.preventDefault();
	 	$('#MenuModulo').animate({'left':'-480px'}, 300);
	},

	initialize: function(){
		this.listenTo(this.model, 'change', this.render);
	},
	render: function () {
	    var botonMenu = this.model.toJSON();
	    var html = this.template(botonMenu);
	    this.$el.html(html);
	    return this;
 	},
}); 

Sistemas.Views.BotonMenuClose = BotonMenuClose;