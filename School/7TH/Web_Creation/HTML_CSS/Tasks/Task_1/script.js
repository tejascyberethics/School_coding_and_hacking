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


const title = document.getElementById("title");
const letters = title.textContent.split("");

// Clear original text content
title.textContent = "";

// Wrap each letter in a span and add it back to the h3
letters.forEach(letter => {
    const span = document.createElement("span");
    span.textContent = letter;
    title.appendChild(span);
});

// Function to apply burst effect
title.addEventListener("click", () => {
    title.querySelectorAll("span").forEach(span => {
        // Generate random values for x, y directions and rotation
        const x = Math.random() * 2 - 1; // Random value between -1 and 1
        const y = Math.random() * 2 - 1; // Random value between -1 and 1
        const rotate = Math.random() * 360 + "deg";

        // Apply random direction and rotation as CSS variables
        span.style.setProperty("--x", x);
        span.style.setProperty("--y", y);
        span.style.setProperty("--rotate", rotate);

        // Add burst animation
        span.style.animation = "burst 0.5s ease forwards";

        // Trigger reappear animation after burst animation ends
        span.addEventListener("animationend", () => {
            span.style.animation = "reappear 0.5s ease forwards";
        }, { once: true }); // Ensure reappear animation only starts once per burst
    });
});


