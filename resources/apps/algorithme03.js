const app = new Vue({
  el: "#simulation-1",
  data: {
    step: -1,
    j1: 0,
    j2: 0,
    objets: ["Pierre", "Feuille", "Ciseaux"],
    message: ''
  },
  methods: {
    setFocus: function (control) {
      const ctrl = this.$refs[control][0];
      ctrl.focus();
      ctrl.select();
    },
    simuler: function (step) {
      this.step = step;
      if (step == 0) {
        this.j1 = Math.floor(Math.random() * 3);
        Vue.nextTick(() => this.setFocus('j1'));
      } else if (step == 1) {
        this.j2 = Math.floor(Math.random() * 3);
        let g = (this.j1 - this.j2) % 3;
        if (g < 0) { g += 3; }
        if (g == 0) {
          this.message = "Match nul";
        } else if (g == 1) {
          this.message = "Bravo, vous gagnez!";
        } else {
          this.message = "Désolé, vous perdez!";
        }
      }
    }
  }
});
