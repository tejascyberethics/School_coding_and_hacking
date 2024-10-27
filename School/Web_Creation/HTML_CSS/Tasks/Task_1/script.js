let buttons = document.querySelectorAll('.btn');
buttons.forEach(buttons => {
    let text = buttons.textContent;
    buttons.innerHTML = '';

    for (let char of text){
        let span = document.createElement('span');
        span.textContent = char === '' ? '\u00A0' : char;
        buttons.appendChild(span);
    }
    let spans = buttons.querySelectorAll('span');

    buttons.addEventListener('mouseenter', () => {
        spans.forEach((spans, index) =>{
            setTimeout(() => {
                spans.classList.add('hover');

            },index * 50);
        })
    })

    buttons.addEventListener('mouseleave', () => {
        spans.forEach((spans, index) =>{
            setTimeout(() => {
                spans.classList.remove('hover');

            },index * 50);
        })
    })
})


