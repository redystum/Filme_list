function add_to_list(film, prepend = false, col = 0) {
    console.log(film)
    let reviews = film.ratingCount;
    if (reviews >= 1000000) {
        reviews = (reviews / 1000000).toFixed(0) + 'M';
    } else if (reviews >= 1000) {
        reviews = (reviews / 1000).toFixed(0) + 'k';
    } else {
        reviews = reviews.toString();
    }
    let elm = `
     <div class="card">
            <img src="${film.image}" class="card-img-top" alt="Film cover">
            <div class="card-body">
                <h5 class="card-title">${film.name}</h5>
                <p class="card-text mb-1">${film.type} <span class="color-soft-secondary">&nbsp; | ${film.year} | ${film.runtime}</span></p>
                <p class="card-text mb-1">${film.genres.join(', ')}</p>
                <p class="card-text"><img src="assets/star.svg" width="16" height="16" alt="Star"> ${film.ratingStars} <span class="color-soft-secondary">(${reviews} reviwes)</span></p>
                <div class="card-tools row">
                    <div href="#" class="col-md-6">
                        <span class="deleteBtn">
                            <span class="material-symbols-outlined icon">
                                delete
                            </span>
                        </span>
                    </div>
                    <div href="#" class="col-md-6 text-end">
                        <span class="doneBtn">
                            Done
                            <span class="material-symbols-outlined icon">
                                done
                            </span>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    `;
    console.log(col)
    if (prepend) {
        $('#filmList .list-col').eq(col).prepend(elm);
    } else {
        $('#filmList .list-col').eq(col).append(elm);
    }
}