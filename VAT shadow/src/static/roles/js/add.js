$(document).ready(function(){
    // let val = $('.id_checkbox_view').val()
    // console.log(val)
    // $('.id_checkbox_view').click(function(){
    //     alert('hi',val)
    //     $('#perm_row')
    // })
    function handleCheckboxInteractions() {
      // Get references to the role checkbox and permission checkboxes
      const roleCheckbox = document.getElementById('id_checkbox_perm');
      const viewCheckboxes = document.querySelectorAll('.id_checkbox_view');
      const addCheckboxes = document.querySelectorAll('.id_checkbox_add');
      const editCheckboxes = document.querySelectorAll('.id_checkbox_edit');
      const deleteCheckboxes = document.querySelectorAll('.id_checkbox_delete');

      // Function to check/uncheck permission checkboxes based on the role checkbox state
      function updatePermissionCheckboxes(isChecked) {
        permissionCheckboxes.forEach((checkbox) => {
          checkbox.checked = isChecked;
        });
        viewCheckboxes.forEach((checkbox) => {
          checkbox.checked = isChecked;
        });
        addCheckboxes.forEach((checkbox) => {
          checkbox.checked = isChecked;
        });
        editCheckboxes.forEach((checkbox) => {
          checkbox.checked = isChecked;
        });
        deleteCheckboxes.forEach((checkbox) => {
          checkbox.checked = isChecked;
        });
      }

      // Role checkbox change event
      roleCheckbox.addEventListener('change', function() {
        const isChecked = this.checked;
        updatePermissionCheckboxes(isChecked);
      });

      // Individual permission checkboxes change events
      viewCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', function() {
          const isChecked = this.checked;
          const permId = this.id.replace('view', '');
          // const correspondingAddCheckbox = document.getElementById(`add${permId}`);
          correspondingAddCheckbox.checked = isChecked;
        });
      });

      addCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', function() {
          const isChecked = this.checked;
          const permId = this.id.replace('add', '');
          const correspondingViewCheckbox = document.getElementById(`view${permId}`);
          // const correspondingEditCheckbox = document.getElementById(`edit${permId}`);
          correspondingViewCheckbox.checked = isChecked;
          // correspondingEditCheckbox.checked = isChecked;
        });
      });

      editCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', function() {
          const isChecked = this.checked;
          const permId = this.id.replace('edit', '');
          const correspondingViewCheckbox = document.getElementById(`view${permId}`);
          const correspondingAddCheckbox = document.getElementById(`add${permId}`);
          correspondingAddCheckbox.checked = isChecked;
          correspondingViewCheckbox.checked = isChecked;
        });
      });

      deleteCheckboxes.forEach((checkbox) => {
        checkbox.addEventListener('change', function() {
          const isChecked = this.checked;
          const permId = this.id.replace('delete', '');
          const correspondingViewCheckbox = document.getElementById(`view${permId}`);
          const correspondingAddCheckbox = document.getElementById(`add${permId}`);
          const correspondingEditCheckbox = document.getElementById(`edit${permId}`);
          const correspondingPermissionCheckbox = document.getElementById(`id_checkbox_perm${permId}`);
          correspondingViewCheckbox.checked = isChecked;
          correspondingAddCheckbox.checked = isChecked;
          correspondingEditCheckbox.checked = isChecked;
          correspondingPermissionCheckbox.checked = isChecked;

          // Check the Role checkbox only when all permission checkboxes are checked
          const allPermissionsChecked =
            [...viewCheckboxes, ...addCheckboxes, ...editCheckboxes, ...deleteCheckboxes].every(
              (checkbox) => checkbox.checked
            );

          roleCheckbox.checked = allPermissionsChecked;
        });
      });
    }

    // Call the function to initialize the interactions
    handleCheckboxInteractions();



    // for (let i =1; i<4;i++){
    //     console.log(i)
    //     let view = 'id_checkbox_view'+i;

    //     $(view).click(function(){
    //         alert('hi')
    //     })

    // }
})