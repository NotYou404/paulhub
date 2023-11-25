function setCookie(name, value, options = {}) {
  options = {
    path: '/',
    ...options
  };

  if (options.expires instanceof Date) {
    options.expires = options.expires.toUTCString();
  }

  let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

  for (let optionKey in options) {
    updatedCookie += "; " + optionKey;
    let optionValue = options[optionKey];
    if (optionValue !== true) {
      updatedCookie += "=" + optionValue;
    }
  }

  document.cookie = updatedCookie;
}

function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

function deleteCookie(name) {
  setCookie(name, "", {
    'max-age': -1
  });
}

const decodingHandler = (() => {
  const element = document.createElement('div');
  return text => ((element.innerHTML = text), element.textContent);
})();

function setHasPremium() {
  return setCookie("hasPremium", "1"); // todo implement this everywhere
}

function clearHasPremium() {
  return deleteCookie("hasPremium");
}

function stopWYG() {
  let wyg_player = document.getElementById("wantYouGonePlayer");
  wyg_player.pause()
  wyg_player.currentTime = 0;
}