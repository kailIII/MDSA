var MenuConfiguracionUsuario = Backbone.View.extend({
	el 		  : $('#Menu-Usuario'),
	tagName   : 'div',
	className : 'Menu-Usuario-Configuracion',
	template  : _.template($('#Menu-Usuario-Configuracion-Template').html()),

	initialize : function(){
		this.listenTo(this.model, 'change', this.render );
	},
	render: function(){
		var menuConfiguracionUsuario = this.model.toJSON();
		var html = this.template(menuConfiguracionUsuario);
		this.$el.html(html);
		return this;
	},
});