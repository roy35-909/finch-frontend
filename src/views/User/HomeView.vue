<template>
    <main-header />
    <section class="hero__section">
        <img 
            class="hero__image" 
            src="https://www.next.co.uk/cms/resource/blob/840444/91cfd22ecdcf5797673d4050efc1accb/200125-block1-hero-dt-live-amend-data.jpg" 
            alt="Hero Section Image"
        />
        <div class="container mx-auto text-center p-4">
            <div class="hero__text">
                <h4 class="text-lg md:text-xl">Trade-in-offer</h4>
                <h3 class="text-2xl md:text-3xl">Super value deals On all products only for ostad</h3>
                <p class="text-lg md:text-xl lg:text-2xl text-white">Save more with coupons & get up to 70% off!</p>
                <router-link to="/shop">
                    <action-button btnvalue="Shop Now" />
                </router-link>
            </div>
        </div>
    </section>
    <advert-section />
    <!-- <service-section /> -->
    <section class="feature__section">
        <div class="container">
            <featured-products :featuredProducts="featuredProducts" />
        </div>
    </section>

    <banner-section />
    <section class="feature__section">
        <div class="container">
            <new-arrivals :newArrivals="newArrivals" />
        </div>
    </section>
    <news-letter />
    <main-footer />
</template>

<script>
import ServiceSection from "@/components/home_components/ServiceSection.vue";
import BannerSection from "@/components/home_components/BannerSection.vue";
import NewArrivals from "@/components/home_components/products/NewArrivals.vue";
import AdvertSection from "@/components/home_components/AdvertSection.vue";
import FeaturedProducts from "@/components/home_components/products/FeaturedProducts.vue";
import ActionButton from "@/components/ActionButton.vue";
import Topbar from "@/components/Topbar.vue";
import MainHeader from "@/components/MainHeader.vue";
import NewsLetter from "@/components/NewsLetter.vue";
import MainFooter from "@/components/MainFooter.vue";
import CategoryBar from "@/components/CategoryBar.vue";

import axios from '@/axios'; 
import { mapActions } from "vuex";

export default {
    name: "HomeView",
    data() {
        return {
            products: [],
        };
    },
    async created() {
        let res1 = await axios.get("/products/");
        this.products = res1.data.results.map((product) => {
            return product;
        });
        this.set_products(this.products);
    },
    computed: {
        featuredProducts() {
            return this.products.filter((product) => product.is_featured);
        },
        newArrivals() {
            return this.products
                .slice() // Create a shallow copy to avoid mutating the original array
                .sort((a, b) => new Date(b.created_at) - new Date(a.created_at)) // Sort by newest first
                .slice(0, 8); // Take the latest 8 products
        },
    },
    methods: {
        ...mapActions(["set_products"]),
    },
    components: {
        ServiceSection,
        BannerSection,
        NewArrivals,
        AdvertSection,
        FeaturedProducts,
        ActionButton,
        MainHeader,
        Topbar,
        NewsLetter,
        MainFooter,
        CategoryBar,
    },
};
</script>

<style scoped>
/* Hero Section */
.hero__section {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: calc(100vh - 65px);
    overflow: hidden;
    padding-block: 10px;
}

.hero__image {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -1;
}

.hero__text {
    position: relative;
    color: white;
    text-shadow: 0 2px 4px rgba(0, 0, 0, 0.6);
    z-index: 1;
}
.container {
    z-index: 1;
    position: relative;
}

.hero__text h4 {
    padding-bottom: 1rem;
}

/* .hero__text h1 {
    color: var(--dim-blue);
} */

.hero__text p {
    margin-bottom: 1rem;
    /* text-shadow: none; */
    font-weight: bold;
}
@media (max-width: 799px) {
    .hero__section {
        height: auto; 
    }

}

@media (min-width: 2000px) {
    .hero__section {
        background-position: 70% 12%;
        background-size: contain;
        background-repeat: no-repeat;
        background-color: #e3e6f3;
        height: 50vh;
    }
}

@media (min-width: 3000px) {
    .hero__section {
        background-position: 60% 30%;
    }
}
</style>
