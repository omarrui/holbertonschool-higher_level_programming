#!/usr/bin/node
document.querySelector('add_item').addEventListener('click', function(){
    const newitem = document.createElement('li');
    newitem.textContent = 'item';
    document.querySelector('.my_list').appendChild(newitem);
});
