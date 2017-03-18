(function($) {
    $.fn.paginator = function(options) {
        var plugin = this;
        var items;

        var defaults = {
            itemsPerPage: 20,
            currentPage: 1
        };
        var settings = {};

        plugin.init = function() {
            $.extend(settings, defaults, options);

            items = $(settings.items);
            var maxPage = Math.ceil(items.length / settings.itemsPerPage);


            for(i = 0; i < maxPage; i++) {
                plugin.append('<li><a href="#">' + (i + 1) + '</a></li>');
            };
            items.filter(':gt(' + (settings.itemsPerPage-1) + ')').hide();
        };

        plugin.init();

        plugin.changePage = function(page) {
            if(page<1 || page>maxPage) {
                return false;
            };
        };

        plugin.drawPagination = function(currentPage) {
            return true;
        };
        
        plugin.children('li').on('click', function() {
            var pageNum = $(this).text();
            console.log(pageNum);

            var itemsToHide = items.filter(':lt(' + ((pageNum - 1) * settings.itemsPerPage) + ')');
            $.merge(itemsToHide, items.filter(':gt(' + ((pageNum * settings.itemsPerPage) - 1) + ')'));
            itemsToHide.hide();
            
            var itemsToShow = items.not(itemsToHide);
            itemsToShow.show();
        });
    };
}(jQuery));