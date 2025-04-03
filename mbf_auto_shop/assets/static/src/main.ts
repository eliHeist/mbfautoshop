import './style.css'
import Alpine from "alpinejs";
import mask from "@alpinejs/mask"
import collapse from "@alpinejs/collapse"
import 'htmx.org';


Alpine.plugin(mask)
Alpine.plugin(collapse)

Alpine.start()