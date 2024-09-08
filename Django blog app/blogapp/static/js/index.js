
// links.forEach(node=>{
//     node.addEventListener("click", function(event){
    //         node.classList.add("active")
//         console.log(node)
//         if(node){
//             links.forEach(newNode=>{
    //                 if(newNode != node){
        //                     newNode.classList.remove("active")
//                 }

//             })
//         }
//     })
// })

document.addEventListener('DOMContentLoaded', function(){
    let currentPath = window.location.pathname
    // console.log(currentPath)
    const links = document.querySelectorAll('.nav-link')

    for(i=0; i < links.length; i++){
        if(links[i].getAttribute('href') === currentPath){
            links[i].classList.add('active')
        }
    }

    // links.forEach(link=>{
    //     if(link.getAttribute('href') === currentPath){
    //         link.classList.add('active')
    //     }
    // })
})

function showBox() {
    let length = 5.0;
    let width = 3.0;
    let height = 2.0;

    let dimensionsText = `Length: ${length} | Width: ${width} | Height: ${height}`;
    let volumeText = `Volume: ${calculateVolume(length, width, height)}`;

    document.getElementById('dimensions').innerText = dimensionsText;
    document.getElementById('volume').innerText = volumeText;

    // Show the box container
    document.getElementById('box-container').style.display = 'block';
}

function calculateVolume(length, width, height) {
    return length * width * height;
}

