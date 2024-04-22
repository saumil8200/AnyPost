console.log("HELLO");

let postsUrl = "http://127.0.0.1:8000/api/posts/"

let getPosts = () => {
    fetch(postsUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        buildPosts(data)
    })
}

let buildPosts = (posts) => {
    let postsWrapper = document.getElementById('posts-wrapper')
    for (let i = 0; posts.length > i; i++){
        let post = posts[i]
        let postCard = `
            <div>
                <div>
                    <h2>${post.title}</h2>
                    <div>
                        <p>${post.description}</p>
                        <p>Total Likes: ${post.likes}</p>
                        <button>LIKE</button>
                        <button>DISLIKE</button>
                    </div>
                </div>
                <!--<img width="100%" src="http://127.0.0.1:8000${post.featured_image}">-->
                <ul>
                    <li>Category: ${post.category.name}</li>
                    <li>Owner: ${post.owner.name}</li>
                    <li>Created At: ${post.created}</li>
                </ul>
            </div>
            <hr>
        `
        postsWrapper.innerHTML += postCard 
    }
}

getPosts()