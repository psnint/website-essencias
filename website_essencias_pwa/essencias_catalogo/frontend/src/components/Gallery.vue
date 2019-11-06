<template>
  <div class="gallery__base">
    <div v-if="loading">
      Loading...
    </div>
    <div v-if="error">
      Couldn't fetch list of products for this catalogue from server...
    </div>
    <div v-if="product">
      <h2 class="gallery__title">1 - {{ product[`title_${$store.getters.lang}`] }}</h2>
      <img class="gallery__image" src="../assets/catalogue/Page-9-2.png" alt="title" />
    </div>
  </div>
</template>

<script>

export default {
  name: 'Gallery',
  data: () => ({
    loading: false,
    error: null,
    product: null,
  }),
  created() {
    this.requestProducts();
  },
  methods: {
    requestProducts() {
      this.products = null;
      this.error = null;
      this.loading = true;
      // Replace by fetch when API is ready
      new Promise((resolve, reject) => {
        resolve({
          pk: '1',
          title_pt: 'Product Title PT',
          title_en: 'Product Title EN',
          title_fr: 'Product Title FR',
          description_pt: 'Product Description PT',
          description_en: 'Product Description EN',
          description_fr: 'Product Description FR',
          image: 'media/images/collections/Teste1',
        });
      }).then((res) => {
        this.loading = false;
        this.product = res;
      }).catch(() => {
        this.loading = false;
        this.error = true;
      });
    },
  },
};

</script>


<style scoped lang="scss">
@import "../css/default.scss";

$moduleName: "gallery";

.#{$moduleName} {
  &__base {
    position: relative;
    max-width: 768px;
    width: 100%;
    margin: auto;
  }

  &__title,
  &__image {
    display: inline-block;
    text-align: center;
    width: 80%;
    margin: auto;
  }

  &__title {
    color: #000;
    font-weight: 300;
    margin: 20px 0;
    text-transform: uppercase;
    font-size: 1rem;

    @include breakpoint-from(mq3) {
      font-size: 1.4rem;
    }
  }

  &__image {
    width: 90%;
  }
}
</style>
