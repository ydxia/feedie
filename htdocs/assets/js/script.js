Function.prototype.inherits = function(cls){
	this.prototype = new cls();
};

Array.prototype.last = function(){
	return this[this.length - 1];
}

function Exception(){
	this.message = Array.prototype.slice.call(arguments, 0).join(", ");
}

/**
 * The base class for interactive objects on the page
 */
function Component(selector, isTemplate){
	if (isTemplate === true){
		this.element = $(selector).clone();
	}
	else {
		this.element = $(selector);
	}
}

/**
 * Assigns children of the object based on a dict mapping from name
 * to selectors
 * 
 * @param {Object} childDict a mapping from names to selectors 
 */
Component.prototype.getChildren = function(childDict){
	if (typeof this.children !== "object"){
		this.children = {};
	}
	for (var key in childDict){
		this.children[key] = this.element.find(childDict[key]);
	}
	return this;
};
Component.prototype.hide = function(){ this.element.hide(); }
Component.prototype.show = function(){ this.element.show(); }

/**
 * The square panel which previews a photo
 */
function Panel(selector, controller){
	Component.call(this, selector);
	
	this.getChildren({
		image: 'img'
	});
	this.controller = controller;
	this.photoId = this.element.data("photo-id");
	this.revealed = false;
	
	this.children.image.on("load", this.revealImage.bind(this));
	if (this.children.image[0].complete){
		this.revealImage();
	}
}
Panel.inherits(Component);

Panel.prototype.setSize = function(width, height){
	this.element.css({
		width: width,
		height: height
	});
}

Panel.prototype.revealImage = function(){
	
	// Make sure the function can only be called once
	if (this.revealed) return;
	this.revealed = true;

	var heightRatio = this.children.image.height() / this.children.image.width();
	if (heightRatio > 1){
		this.children.image.css({
			width: "100%",
			top: (heightRatio - 1) * -50 + "%"
		});
	}
	else {
		this.children.image.css({
			height: "100%",
			left: (1 / heightRatio - 1)* -50 + "%"
		});
	}
	this.element.addClass("image-ready").click(function(){
		this.controller.openPhotoBoxForPanel(this);
	}.bind(this));
}

/**
 * Sets the next or previous panel in the list of panels 
 *
 * @param {Panel} panel the next/previous panel in the view
 */
Panel.prototype.setNext = function(panel){
	this.next = panel;
};
Panel.prototype.setPrev = function(panel){
	this.prev = panel;
};


function SelectRow(selector){
	Component.call(this, selector);
	this.getChildren({
		options: ".option",
		selected: ".options.selected",
		underline: ".underline"
	});
	this.changeCallback = function(){};
	
	if (this.children.selected.length){
		this.value = this.children.selected.data("value");
		this.children.underline.css("left", this.children.selected);
	}
	
	var optionWidth = 100 / this.children.options.length;
	this.children.options.outerWidth(optionWidth + "%");
	this.children.underline.outerWidth(optionWidth + "%");
	
	// Shift the underline when a new option is selected
	var selectRow = this;
	this.children.options.each(function(i){
		$(this).click(function(){
			if ($(this).data("value") == selectRow.value) return;
			
			selectRow.value = $(this).data("value");
			selectRow.children.underline.css("left", i * optionWidth + "%");
			selectRow.children.selected.removeClass("selected");
			selectRow.children.selected = $(this).addClass("selected");
			selectRow.changeCallback(selectRow.value);
		});
	});
}
SelectRow.inherits(Component);

SelectRow.prototype.onChange = function(callback){
	this.changeCallback = callback;
};

/**
 * The popout box that displays the info for the photo
 */
function PhotoBox(selector){
	Component.call(this, selector);
	this.getChildren({
		background: "#background",
		imageContainer: "#photo",
		image: "#photo img",
		scrollArea: "#scroll-area",
		handle: ".user-handle",
		description: ".description",
		date: "#date",
		recipe: "#recipe",
		closeButton: "#close",
		photoMenu: "#photo-menu",
		photoMenuButton: "#photo-menu-button",
		favouriteButton: "#favourite-button"
	});
	
	this.children.closeButton.click(this.hide.bind(this));
	this.children.photoMenuButton.click(this.togglePhotoMenu.bind(this));
	this.children.favouriteButton.click(this.favouritePhoto.bind(this));
	$(window).resize(this.adjustPhoto.bind(this));
}
PhotoBox.inherits(Component);

/**
 * Opens the photo box. If no arguments are supplied, it will just
 * fade in. If a Panel is passed, it will expand from the bounds
 * of the Panel
 *
 * @param {Panel} panel the object that is to be expanded from
 */
PhotoBox.prototype.show = function(panel){
	
	if (panel === undefined){
		this.children.background.css({
			opacity: 0,
			filter: "alpha(opacity=0)"
		}).addClass("show");
	}
	else {
		this.referencedPanel = panel;
	
		// Get the element's position on the screen
		var top = panel.element.offset().top - $(window).scrollTop();
		var left = panel.element.offset().left - $(window).scrollLeft();
		
		this.children.background.css({
			width: panel.element.outerWidth(),
			height: panel.element.outerHeight(),
			top: top,
			left: left
		});
		this.element.addClass('show');
		this.children.scrollArea.scrollTop(0);
	}
	
	$("body").addClass("no-scroll");
	setTimeout(function(){
		this.children.background.removeAttr("style");
	}.bind(this), 0);
	
	setTimeout(function(){
		this.element.addClass("full");
		this.adjustPhoto();
	}.bind(this), 500);
};

/** 
 * Closes the photo box. If there is no referenced Panel, it will just
 * fade out. If there is a referenced Panel, it will shrink into the 
 * position of its element.
 */
PhotoBox.prototype.hide = function(){
	this.element.removeClass("full").addClass("hiding");
	this.togglePhotoMenu(false);

	if (!this.referencedPanel){
		this.children.background.css({
			opacity: 0,
			filter: "alpha(opacity=0)"
		});
	}
	else {
		var panel = this.referencedPanel;
		this.referencedPanel = undefined;
	
		// Get the element's position on the screen
		var top = panel.element.offset().top - $(window).scrollTop();
		var left = panel.element.offset().left - $(window).scrollLeft();
	
		this.children.background.css({
			width: panel.element.outerWidth(),
			height: panel.element.outerHeight(),
			top: top,
			left: left
		});
	}
	
	setTimeout(function(){
		this.element.removeClass("show").removeClass("hiding");
		$("body").removeClass("no-scroll");
	}.bind(this), 500);
};

/** 
 * Load a photo and the information into the photo box
 *
 * @param {string} photoId the unique identifier of the photo
 * @param {function} callback a function that is run once the image 
 *                            is loaded
 */
PhotoBox.prototype.load = function(photoId, callback){
	// Do ajax things and requests
	callback();
};

PhotoBox.prototype.loadByPanel = function(panel){
	this.load(panel.photoId, function(){
		this.show(panel);
	}.bind(this));
};

PhotoBox.prototype.loadByPhotoId = function(photoId){
	this.load(panel.photoId, function(){
		this.show();
	}.bind(this));
};

/** 
 * Adjust the position of the photo 
 */
PhotoBox.prototype.adjustPhoto = function(){
	var imageHeight = this.children.image.height();
	var containerHeight = this.children.imageContainer.height();
	if (imageHeight < containerHeight){
		this.children.image.css("margin-top", (containerHeight - imageHeight) / 2);
	}
	else {
		this.children.image.css("margin-top", 0);
	}
};

/**
  * Toggles the view of the photo menu
  *
  * @param {boolean=} show Determines whether to show or hide the menu
  */
PhotoBox.prototype.togglePhotoMenu = function(show){
	this.element.toggleClass("show-photo-menu", show);
	this.children.photoMenuButton.toggleClass("close", show);
};

PhotoBox.prototype.favouritePhoto = function(){
	if (this.favourited) return;
	
	// TODO: Ajax call to try to favourite the photo
	this.element.addClass("favourited");
};

function PageHeader(elem, controller){
	Component.call(this, elem);
	
	this.getChildren({
		menuButton: "#menu-button"
	});
	this.children.menuButton.click(controller.toggleLeftMenu.bind(controller));
}
PageHeader.inherits(Component);

function PageController(){
	this.panels = [];
	this.panelMapping = {};
	this.DESKTOP_MIN_WIDTH = 1000;

	$(function(){
		this.initPage();
	}.bind(this));
}

PageController.prototype.initPage = function(){
	try {
		this.photoBox = new PhotoBox("#photo-box");
		this.pageHeader = new PageHeader("#header", this);
		this.feedSelector = new SelectRow("#feed-selector");
		
		if ($(window).width() > this.DESKTOP_MIN_WIDTH){
			this.toggleLeftMenu(true);
		}
		
		var controller = this;
		$(".panel").each(function(){
			controller.addPanel(this);
		});
		$(window).on("load resize", this.adjustPanelSizes.bind(this));
		
		// Closes the menu when tapping outside of it
		$("#page-content").on("mousedown touchstart", function(){
			if ($(window).width() < this.DESKTOP_MIN_WIDTH){
				this.toggleLeftMenu(false);
			}
		}.bind(this));
	}
	catch (e){
		throw e.constructor.name + ": " + e.message;
	}
};

PageController.prototype.addPanel = function(element){
	var panel = new Panel(element, this);
	
	if (this.panels.length){
		panel.setPrev(this.panels.last());
		this.panels.last().setNext(panel);
	}
	this.panels.push(panel);
	this.panelMapping[panel.photoId] = panel;
};

PageController.prototype.adjustPanelSizes = function(){
	var panelsPerRow = Math.ceil($("#page-content").width() / 300);
	var height = $("#page-content").width() / panelsPerRow;
	for (var i = 0; i < this.panels.length; i++){
		this.panels[i].setSize(100/panelsPerRow + "%", height);
	}
};

PageController.prototype.openPhotoBoxForPanel = function(panel){
	this.photoBox.loadByPanel(panel);
};

/**
  * Toggles the view of the left side menu
  *
  * @param {boolean=} show Determines whether to show or hide the menu
  */
PageController.prototype.toggleLeftMenu = function(show){
	$("body").toggleClass("show-left-menu", show);
	this.pageHeader.children.menuButton.toggleClass("close", show);
	
	setTimeout(this.adjustPanelSizes.bind(this), 500);
};