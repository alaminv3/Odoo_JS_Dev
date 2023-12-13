/** @odoo-module **/

import { SignTemplateIframe } from "@sign/backend_components/sign_template/sign_template_iframe";
import { SignItemCustomPopover } from "@sign/backend_components/sign_template/sign_item_custom_popover";


export class CustomSignTemplateIframe extends SignTemplateIframe {
    constructor(root, env, owlServices, props){
        super(root, env, owlServices, props)
        this.signModelsById = this.props.signModels.reduce((obj, model) => {
            obj[model.id] = model;
            return obj;
        }, {});
//        this.signModelsById = {}
        this.signModelFieldsById = {}
    }

    /**
     * Extends the rendering context of the sign item based on its data
     * @param {SignItem.data} signItem
     * @returns {Object}
     */
    getContext(signItem) {
        super.getContext(signItem)
        const model_model = signItem.model_model ?? (signItem.model_id?.[0] || 1);
        const model_field = signItem.model_field ?? (signItem.field_id?.[0] || 1);
        return Object.assign(signItem, {
            model_model,
            model_field,
        });
    }

    /**
     * Handles opening and closing of popovers in template edition
     * @param {SignItem} signItem

     This method is overridden. Cause we have to add our custom methods related to models and fields
     into the iframe so that we can use them in popover validate.
     */
    async openSignItemPopup(signItem) {
        const shouldOpenNewPopover = !(signItem.data.id in this.closePopoverFns);
        this.closePopover();
        if (shouldOpenNewPopover) {
            if (signItem.data.id in this.negativeIds) {
                await this.negativeIds[signItem.data.id];
            }
            const closeFn = this.popover.add(
                signItem.el,
                SignItemCustomPopover,
                {
                    debug: this.env.debug,
                    responsible: signItem.data.responsible,
                    roles: this.signRolesById,
                    alignment: signItem.data.alignment,
                    required: signItem.data.required,
                    placeholder: signItem.data.placeholder,
                    id: signItem.data.id,
                    type: signItem.data.type,
                    option_ids: signItem.data.option_ids,
                    onValidate: (data) => {
                        this.updateSignItem(signItem, data);
                        this.closePopover();
                    },
                    onDelete: () => {
                        this.closePopover();
                        this.deleteSignItem(signItem);
                    },
                    onClose: () => {
                        this.closePopover();
                    },
                    updateSelectionOptions: (ids) => this.updateSelectionOptions(ids),
                    updateRoles: (id) => this.updateRoles(id),
                    updateModels: (id) => this.updateModels(id),
                    updateModelFields: (id) => this.updateModelFields(id),
                },
                {
                    position: "right",
                    onClose: () => {
                        this.closePopoverFns = {};
                    },
                }
            );
            this.closePopoverFns[signItem.data.id] = {
                close: closeFn,
                signItem,
            };
        }
    }

    /**
     * Updates the local signModelsById to include new records
     * @param {Number} id role id
     */
    async updateModels(id) {
        if (!(id in this.signModelsById)) {
            const newModel = await this.orm.searchRead("ir.model", [["id", "=", id]], [], {
                context: this.user.context,
            });
            this.signModelsById[newModel[0].id] = newModel[0];
        }
    }

    /**
     * Updates the local signModelFieldsById to include new records
     * @param {Number} id role id
     */
    async updateModelFields(id) {
        if (!(id in this.signModelFieldsById)) {
            const newModelFields = await this.orm.searchRead("ir.model.fields", [["id", "=", id]], [], {
                context: this.user.context,
            });
            this.signModelFieldsById[newModelFields[0].id] = newModelFields[0];
        }
    }
}