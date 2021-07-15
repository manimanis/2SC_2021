$(() => {
  const qNav = $('#question-navigation');
  const ul = $('ul.pagination', qNav);
  const questions = $('.question');
  const topics = $('.topic');

  function displayQuestion(index) {
    topics.hide();
    questions.hide();
    const question = questions.eq(index);
    question
      .show();
    question
      .closest('.topic').show();
    $('li', qNav)
      .removeClass('active')
      .eq(index)
      .addClass('active');
  }

  questions.each(function (index) {
    const question = $(this);
    const isAnswered = question.hasClass('text-success');
    const li = $('<li>')
      .addClass('page-item')
      .appendTo(ul);
    const a = $('<a>')
      .addClass('page-link')
      .attr('href', '#q_' + index)
      .html(`${(isAnswered) ? '<u>' : ''}${index +1}${(isAnswered) ? '</u>' : ''}`)
      .appendTo(li)
      .click((e) => {
        e.preventDefault();
        const target = e.currentTarget;
        const href = $(target).attr('href');
        const numq = parseInt(href.substr(3));
        displayQuestion(numq);
      });
  });

  displayQuestion(0);
});