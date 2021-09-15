$(() => {
  const curPos = new URL(location.href);
  let sectionNum = -1;
  let articleNum = -1;
  if (curPos.hash.startsWith("#section")) {
    const hs = curPos.hash.split('-');
    articleNum = +hs[1] - 1;
    sectionNum = +hs[2] - 1;
  }

  const aside = $('aside #aside_navbar');
  const articles = $('main article');
  const articles_count = articles.length;
  const STORAGE_KEY = location.pathname + '#art_obj';
  const localStorageData = JSON.parse(localStorage.getItem(STORAGE_KEY)) || {
    article: null,
    article_index: 0,
    sections: null,
    section: null,
    section_index: 0
  };
  const art_obj = (sectionNum != -1 && articleNum != -1) ? {
    article: null,
    article_index: articleNum,
    sections: null,
    section: null,
    section_index: sectionNum
  } : localStorageData;

  const link_list = $('<ul>')
    .addClass('navbar-nav mr-auto')
    .appendTo(aside);

  // hide all articles
  articles
    .addClass('d-none d-print-block')
    .each((index, art_elem) => {
      const article = $(art_elem);
      const id = `article-${index + 1}`;
      const title = article.find('h2').text();

      // article
      //   .attr('id', id);

      const li = $('<li>')
        .addClass('nav-item dropdown')
        .appendTo(link_list);
      const a_id = `link-${index + 1}`;
      const a = $('<a>')
        .addClass('nav-link dropdown-toggle')
        .attr('href', `#${id}`)
        .attr('id', a_id)
        .attr('role', 'button')
        .attr('data-bs-toggle', 'dropdown')
        .attr('aria-haspopup', 'true')
        .attr('aria-expanded', 'false')
        .text(title)
        .appendTo(li);

      const sections = article.find('section');
      if (sections.length) {
        const sect_list = $('<div>')
          .attr('aria-labelledby', a_id)
          .addClass('dropdown-menu')
          .appendTo(li);
        sections
          .each((section_index, sect_elem) => {
            const section = $(sect_elem);
            const id = `section-${index + 1}-${section_index + 1}`;
            const a_id = `link-${index + 1}-${section_index + 1}`;
            const title = section.find('h3').text() || `Page ${section_index + 1}`;
            section
              // .attr('id', id)
              .addClass('d-none d-print-block');
            const a = $('<a>')
              .attr('href', `#${id}`)
              .attr('id', a_id)
              .addClass('dropdown-item')
              .text(title)
              .appendTo(sect_list);
          });
      }
    });

  const displayArticle = (index) => {
    if (art_obj.article && art_obj.article.addClass) {
      art_obj.article
        .addClass('d-none');
      $(`a#link-${art_obj.article_index + 1}`)
        .removeClass('active');
      $(`a#link-${art_obj.article_index + 1}-${art_obj.section_index + 1}`)
        .removeClass('active');
    }
    art_obj.article_index = index;
    art_obj.article = articles.eq(index)
      .removeClass('d-none');
    art_obj.sections = art_obj.article.find('section');
    $(`a#link-${index + 1}`)
      .addClass('active');
  };

  const displaySection = (index) => {
    if (art_obj.section && art_obj.section.addClass) {
      art_obj.section
        .addClass('d-none');
      $(`a#link-${art_obj.article_index + 1}-${art_obj.section_index + 1}`)
        .removeClass('active');
    }
    art_obj.section_index = index;
    art_obj.section = art_obj.sections.eq(index)
      .removeClass('d-none');
    $(`a#link-${art_obj.article_index + 1}-${index + 1}`)
      .addClass('active');

    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      article_index: art_obj.article_index,
      section_index: art_obj.section_index
    }));
  };

  const linkClickHandler = e => {
    // e.preventDefault();
    const link = $(e.currentTarget);
    const href = link.attr('href');
    const href_parts = href.split('-');
    if (href_parts.length >= 3) {
      displayArticle(+href_parts[1] - 1);
      displaySection(+href_parts[2] - 1);
    }
  };

  const pageLinks = $("a[href^=\"#section\"]")
    .click(linkClickHandler);
  // const links = aside.find('a')
  //   .click(linkClickHandler);
  displayArticle(art_obj.article_index);
  displaySection(art_obj.section_index);
});