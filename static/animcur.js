function getCenter(element) {
    const {left, top, width, height} = element.getBoundingClientRect();
    return {x: left + width / 2, y: top + height / 2}
}

const arrow = document.querySelector("#shark");
const arrowCenter = getCenter(arrow);
addEventListener("mousemove", ({clientX, clientY}) => {
    const angle = Math.atan2(clientY - arrowCenter.y, clientX - arrowCenter.x);
    arrow.style.transform = `rotate(${angle}rad)`;
});