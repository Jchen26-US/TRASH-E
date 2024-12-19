// Function to refresh image periodically every 5 seconds
setInterval(() => {
    refreshImage("image", "image2", "images/received_img.jpg", "images/annotated_img.jpg");
}, 5000); // 5000 ms = 5 seconds

// Function to refresh image by appending a unique timestamp
function refreshImage(imageId, imageId2, imageUrl, imageUrl2) {
    const image = document.getElementById(imageId);
    const image2 = document.getElementById(imageId2);
    image.src = `${imageUrl}?t=${new Date().getTime()}`;
    image2.src = `${imageUrl2}?t=${new Date().getTime()}`;
}

// Optional: Button for manual refresh
function manualRefresh() {
    refreshImage("image", "images/annotated_img.jpg");
}
