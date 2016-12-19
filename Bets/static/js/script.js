$(function() {
    function validateForm() {
        $('.text-error').remove();
        var v_name = false;
        var v_sport = false;
        var v_country = false;
        var v_coach = false;
        var v_games = false;
        var v_win = false;
        var v_description = false;
        var v_logo = false;

        var el_n = $('#name');
        if (el_n.val().length > 30){
            v_name = true;
            $('.team-name').after('<span class="text-error">Название команды должно быть меньше 30 символов</span>');
        }
        if (el_n.val().length == 0){
            v_name = true;
            $('.team-name').after('<span class="text-error">Поле не может быть пустым</span>');
        }

        var el_s = $('#sport');
        if (el_s.val().length > 30){
            v_sport = true;
            $('.team-sport').after('<span class="text-error">Название вида спорта должно быть меньше 30 символов</span>');
        }
        if (el_s.val().length == 0){
            v_sport = true;
            $('.team-sport').after('<span class="text-error">Поле не может быть пустым</span>');
        }

        var el_c = $('#country');
        if (el_c.val().length > 30){
            v_country = true;
            $('.team-country').after('<span class="text-error">Название страны должно быть меньше 30 символов</span>');
        }
        if (el_c.val().length == 0){
            v_country = true;
            $('.team-country').after('<span class="text-error">Поле не может быть пустым</span>');
        }

        var el_coach = $('#coach');
        if (el_coach.val().length > 50){
            v_coach = true;
            $('.team-coach').after('<span class="text-error">Имя тренера должно быть меньше 50 символов</span>');
        }
        if (el_coach.val().length == 0){
            v_coach = true;
            $('.team-coach').after('<span class="text-error">Поле не может быть пустым</span>');
        }

        var el_g = $('#games');
        if (el_g.val().length > 5){
            v_games = true;
            $('.team-games').after('<span class="text-error">Слишком большое число</span>');
        }
        if (el_g.val().length == 0){
            v_games = true;
            $('.team-games').after('<span class="text-error">Поле не может быть пустым</span>');
        }
        var value_check = parseInt((el_g.val()));
        if (isNaN(value_check)){
            v_games = true;
            $('.team-games').after('<span class="text-error">Можно вводить только числа</span>');
        }

        var el_w = $('#win');
        if (el_w.val().length > 5){
            v_win = true;
            $('.team-win').after('<span class="text-error">Слишком большое число</span>');
        }
        if (el_w.val().length == 0){
            v_win = true;
            $('.team-win').after('<span class="text-error">Поле не может быть пустым</span>');
        }
        value_check = parseInt((el_w.val()));
        if (isNaN(value_check)){
            v_win = true;
            $('.team-win').after('<span class="text-error">Можно вводить только числа</span>');
        }

        var el_d = $('#description');
        if (el_d.val().length == 0){
            v_description = true;
            $('.team-description').after('<span class="text-error">Поле не может быть пустым</span>');
        }

        if ($('form input[type=file]').val().length == 0){
            v_logo = true;
            $('.team-logo').after('<span class="text-error">Выберите файл</span>');
        }

        return (v_name || v_sport || v_country || v_coach || v_games || v_win || v_description || v_logo);
    }

    $('.add_team').on('submit', function (event) {
        if (validateForm()) {
            event.preventDefault();
        }
    });
    
    $('.btn-close').click(function () {
        $('#name').val('');
        $('.text-error').remove();
    })
});
