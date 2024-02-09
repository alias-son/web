import Home from './components/Home.svelte';
import Post from './components/Post.svelte';
import CreatePost from './components/CreatePost.svelte';

const routes = {
    '/': Home,
    '/post/:id': Post,
    '/create': CreatePost
};

export default routes;
