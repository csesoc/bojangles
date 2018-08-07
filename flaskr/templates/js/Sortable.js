// reordering sort preferences
var source;

function isbefore(a, b) {
    if (a.parentNode == b.parentNode) {
        for (var cur = a; cur; cur = cur.previousSibling) {
            if (cur === b) {
                return true;
            }
        }
    }
    return false;
}

function dragenter(e) {
    if (isbefore(source, e.target)) {
        e.target.parentNode.insertBefore(source, e.target);
    }
    else {
        e.target.parentNode.insertBefore(source, e.target.nextSibling);
    }
}

function dragstart(e) {
    source = e.target;
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/plain',null)
}


// adding and removing courses
function addCourse(){
    // get class & info then:
    var courseList = document.getElementById("AllChosenCourses");
    
}

// removing course

function removeCourse(btn){
    console.log("button pressed");
    (((btn.parentNode).parentNode).parentNode).removeChild((btn.parentNode).parentNode);
}

removeButtons = document.querySelectorAll('rmButton');
console.log(removeButtons.length);

for (var i = 0; i < removeButtons.length; i ++) {
    console.log("hi");
    removeButtons[i].addEventListener('click', function() {removeCourse(this)}, false);
}
