var MenuGrafico = Backbone.View.extend({
	tagName   : 'li',
	className : 'Item', 
	//template  : Handlebars.compile($('#MenuGrafico-Template').html()),
	template  : _.template($('#MenuGrafico-Template').html()),
	events : {

	},
	initialize : function() {
	   this.listenTo(this.model, 'change', this.render);
	   
	},

	render: function () {
	    var menuGrafico = this.model.toJSON();
	    var html = this.template(menuGrafico);
	    this.$el.html(html);
	    return this;
 	},
});

Sistemas.Views.MenuGrafico = MenuGrafico;