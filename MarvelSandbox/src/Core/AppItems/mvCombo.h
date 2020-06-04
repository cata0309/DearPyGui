#pragma once

#include "Core/mvAppItem.h"

namespace Marvel {

	class mvCombo : public mvAppItem
	{

	public:

		MV_APPITEM_TYPE(mvAppItemType::Combo)

		mvCombo(const std::string& parent, const std::string& name, const std::vector<std::string>& itemnames, const std::string& default_value)
			: mvAppItem(parent, name), m_names(itemnames), m_value(default_value)
		{
		}

		virtual PyObject* getPyValue() override
		{
			PyObject* pvalue = Py_BuildValue("s",m_value.c_str());
			return pvalue;
		}

		virtual void draw() override
		{

			if (ImGui::BeginCombo(m_label.c_str(), m_value.c_str())) // The second parameter is the label previewed before opening the combo.
			{
				for (int i = 0; i < m_names.size(); i++)
				{
					bool is_selected = (m_value == m_names[i]);
					if (ImGui::Selectable(m_names[i].c_str(), is_selected))
					{
						m_value = m_names[i];
						mvApp::GetApp()->triggerCallback(m_callback, m_name);
					}

					if (is_selected)
						ImGui::SetItemDefaultFocus();   // Set the initial focus when opening the combo (scrolling + for keyboard navigation support in the upcoming navigation branch)
				}
				ImGui::EndCombo();
			}
		}

	private:

		std::vector<std::string> m_names;
		std::string              m_value;

	};

}