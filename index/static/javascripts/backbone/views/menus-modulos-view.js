var MenusModulos = Backbone.View.extend({
	el 			: $('#Modulos'),
	template 	: _.template($('#MenuModulo-Template').html()),

	initialize:function(){
		this.listenTo(this.collection, 'add', this.agregar, this);
	},
	render:function(){
		this.collection.forEach(this.agregar, this);
	},
	agregar:function(menuModulo){
		var menuModulo = new Sistemas.Views.MenuModulo({model:menuModulo});
		this.$el.append(menuModulo.render().el);
	},
});

Sistemas.Views.MenusModulos = MenusModulos;