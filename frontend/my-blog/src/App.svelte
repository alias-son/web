<script>
import { Router } from 'svelte-spa-router';
import routes from './routes';
</script>

<Router {routes} />

<!-- <main>
	<Router {routes} />
	<h1>Welcome to My Blog!</h1>
	<p>This is the beginning of my personal blog project.</p>
</main> -->

<!-- <style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style> -->