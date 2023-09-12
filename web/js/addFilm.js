
$('#addFilm').click(function () {
    let title = $('#filmTitle').val();
    eel.add_film(title)
    $('#filmTitle').val('');
});

eel.expose(addFilm);
function addFilm(film) {
    add_to_list(film, true);
}