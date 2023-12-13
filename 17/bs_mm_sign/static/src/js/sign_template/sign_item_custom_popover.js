/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import {
    many2ManyTagsField,
    Many2ManyTagsField,
} from "@web/views/fields/many2many_tags/many2many_tags_field";
import { SignItemCustomPopover } from "@sign/backend_components/sign_template/sign_item_custom_popover";
import { useState } from "@odoo/owl";

const actionFieldsGet = {
    option_ids: { type: "many2many", relation: "sign.item.option", string: "Selected Options" },
    responsible_id: { type: "many2one", relation: "sign.item.role", string: "Responsible" },
    model_id: { type: "many2one", relation: "ir.model", string: "Model" },
    field_id: { type: "many2one", relation: "ir.model.fields", string: "Model Field" },
};

function getActionActiveFields() {
    const activeFields = {};
    for (const fName of Object.keys(actionFieldsGet)) {
        if (actionFieldsGet[fName].type === "many2many") {
            const related = Object.fromEntries(
                many2ManyTagsField.relatedFields({ options: {} }).map((f) => [f.name, f])
            );
            activeFields[fName] = {
                related: {
                    activeFields: related,
                    fields: related,
                },
            };
        } else {
            activeFields[fName] = actionFieldsGet[fName];
        }
    }
    return activeFields;
}

patch(SignItemCustomPopover.prototype, {
    setup(){
        super.setup();
        this.state = useState({
            ...this.state,
            model_model: this.props.model_model,
            model_field: this.props.model_field
        });
        this.signItemFieldsGet = getActionActiveFields();
    },

    get relational_model(){

        /* Will use for trace
        console.log('THIS custom ------->>>',this)
        console.log('THIS this.props ------->>>',this.props)*/
        return this.state.model_model;
    },

    get recordProps() {
        return {
            mode: "edit",
            resModel: "sign.item",
            resId: this.props.id,
            fieldNames: this.signItemFieldsGet,
            activeFields: this.signItemFieldsGet,
            onRecordChanged: async (record, changes) => {
                if (changes.option_ids) {
                    let added_ids = [], removed_ids = [];
                    for (let item of changes.option_ids){
                        if(item[0] == 3){
                            removed_ids.push(item[1]);
                        } else if(item[0] == 4){
                            added_ids.push(item[1]);
                        }
                    }
                    let newOptionIds = [...new Set([...this.state.option_ids, ...added_ids])];
                    newOptionIds = newOptionIds.filter(option_id => !removed_ids.includes(option_id));
                    this.state.option_ids = newOptionIds;
                    return this.props.updateSelectionOptions(newOptionIds);
                }
                if (changes.model_id) {
                    const id = changes.model_id;
                    this.state.model_model = id;
                    this.props.updateModels(id);
                }
                if (changes.field_id) {
                    const id = changes.field_id;
                    this.state.model_field = id;
                    this.props.updateModelFields(id);
                }
                if (changes.responsible_id) {
                    const id = changes.responsible_id;
                    this.state.responsible = id;
                    this.props.updateRoles(id);
                }
            },
        };
    }
})