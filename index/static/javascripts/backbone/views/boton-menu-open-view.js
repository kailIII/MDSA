var BotonMenuOpen = Backbone.View.extend({
	tagName   : 'a',
	className : 'Menu-Boton-Link', 
	el 		  : $('#Menu-Boton-Open'),
	//template  : Handlebars.compile($('#BotonMenu-Open-Template').html()),
	template  : _.template($('#BotonMenu-Open-Template').html()),
	events : {
		'click #Menu-Open' : 'openMenu',
	},

	openMenu:function (e) {
	 	e.preventDefault();
	 	$('#MenuModulo').animate({'left':'0'}, 300);
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

Sistemas.Views.BotonMenuOpen = BotonMenuOpen;