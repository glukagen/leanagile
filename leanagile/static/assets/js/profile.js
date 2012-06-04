var imgs = [
	'/static/assets/img/n_circle.png',
	'/static/assets/img/i_circle.png',
	'/static/assets/img/d_circle.png',
	'/static/assets/img/n_circle.png'
],
level_classes = [
	'level_n_status',
	'level_i_status',
	'level_d_status',
	'level_n_status'
]

$(function(){	
	$('.edit_form').submit(function(){
		if($.trim($(this).find('[name=first_name]').val()) == ''){
			alert('Please enter first name')
			return false
		}
		
		if($.trim($(this).find('[name=last_name]').val()) == ''){
			alert('Please enter last name')
			return false
		}
		
		if($.trim($(this).find('[name=last_name]').val()) == ''){
			alert('Please enter specialities')
			return false
		}
		var loader = $(this).find('loader')
		loader.show()
		$(this).ajaxSubmit({
			success: function(id){
				loader.hide()
				alert('Student was successfully updated')
			}
		})
		return false
	})
					
	$('.skill_circle').click(function(){
		var index = $.inArray($(this).find('img').attr('src'), imgs)
		$(this).find('img').attr('src', imgs[index+1])
		
		$.post('/skill/change_status/' + $(this).attr('status_id') + '/', {csrfmiddlewaretoken:csrf_token}, function(o){
		})
	})
	
	$('.btn_level').click(function(){
		var self = $(this)
		var index = $.inArray(self.attr('color_class'), level_classes)
		
		function set_color(element, indexColor){
			var div = element.find('div')
			for(i in level_classes)
				div.removeClass(level_classes[i])
			
			div.addClass(level_classes[indexColor])
			element.attr('color_class', level_classes[indexColor])
		}
		
		set_color(self, index + 1)
		
		var status_is_set = false
		self.parent().find('.btn_level').each(function(){
			if (status_is_set)
				set_color($(this), 0)
			else 
				if (self.attr('level_id') == $(this).attr('level_id')) 
					status_is_set = true
				else 
					set_color($(this), 2)
		})
		
		var value = self.attr('value')
		$.get('/skill/change_progress_status/' + self.attr('status_id') + '/', {
			csrfmiddlewaretoken:csrf_token,
			level: self.attr('level_id'),
			value: value == 'n' ? 'i': value == 'i' ? 'd' : 'n',
			}, function(o){
		})
	})
})