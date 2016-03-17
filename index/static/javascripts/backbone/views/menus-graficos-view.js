var MenusGraficos = Backbone.View.extend({
	el 		 : $('#MenuGrafico'),
	template : _.template($('#MenuGrafico-Template').html()),

	initialize: function () {
	    this.listenTo(this.collection, "add", this.agregar, this);
	},

	render: function () {
	    this.collection.forEach(this.agregar, this);
	},

	agregar: function (menuGrafico) {
	    var menuGrafico = new Sistemas.Views.MenuGrafico ({ model: menuGrafico });
	    this.$el.append(menuGrafico.render().el);
	}
});

Sistemas.Views.MenusGraficos = MenusGraficos;
