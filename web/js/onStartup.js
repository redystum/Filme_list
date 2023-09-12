
$(document).ready(async function () {
    await eel.get_all()().then(function (result) {
        console.log(result)
        let col = 0;
        for (let film of result) {
            add_to_list(film, false, col);
            col++;
            if (col > 3) {
                col = 0;
            }
        }
    });
});