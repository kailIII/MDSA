var MenuModulo = Backbone.View.extend({
	tagName  : 'li',
	className: 'Modulos-Item',
	template : _.template($('#MenuModulo-Template').html()),

	initialize:function () {
		this.listenTo(this.model, 'change', this.render );
	},

	render:function(){
		var menuModulo = this.model.toJSON();
		var html = this.template(menuModulo);
		this.$el.html(html);
		return this;
	},
});

Sistemas.Views.MenuModulo = MenuModulo;