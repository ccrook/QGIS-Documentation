# -*- coding: utf-8 -*-
#
# QGIS Workshop documentation build configuration file, created by
# sphinx-quickstart on Fri Jul  1 14:40:42 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.pngmath']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['../templates']


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'QGIS Documentation Project'
copyright = u'2012, QGIS project'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.0.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = en

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['buildout', 'build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

rst_prolog = """
.. role:: disclaimer
.. |updatedisclaimer| replace:: :disclaimer:`DISCLAIMER: This section of the user guide has not yet been updated for QGIS 2.0`
"""

rst_epilog = """
.. |nix| image:: /static/common/nix.png
   :width: 1em
.. |win| image:: /static/common/win.png
   :width: 1em
.. |osx| image:: /static/common/osx.png
   :width: 1em
.. |QG| replace:: QGIS
.. |CURRENT| replace:: 2.0.0
.. |degrees| unicode:: 0x00B0
   :ltrim:
.. |geographic| image:: /static/common/geographic.png
.. |wedge| unicode:: 0x005e
.. |checkbox| image:: /static/common/checkbox.png
.. |checkbox_checked| image:: /static/common/checkbox.png
.. |checkbox_unchecked| image:: /static/common/checkbox_unchecked.png
.. |radiobuttonon| image:: /static/common/radiobuttonon.png
.. |radiobuttonoff| image:: /static/common/radiobuttonoff.png
.. |selectnumber| image:: /static/common/selectnumber.png
.. |selectstring| image:: /static/common/selectstring.png
.. |browsebutton| image:: /static/common/browsebutton.png
.. |selectcolor| image:: /static/common/selectcolor.png
.. |slider| image:: /static/common/slider.png
.. |inputtext| image:: /static/common/inputtext.png
.. |tab| image:: /static/common/tab.png
.. |calendarwidget| image:: /static/common/calendarwidget.png
   :width: 1.5em
.. |color|  image:: /static/common/color.png
   :width: 1.5em
.. |colormap|  image:: /static/common/colormap.png
   :width: 1.5em
.. |columnview|  image:: /static/common/columnview.png
   :width: 1.5em
.. |combobox|  image:: /static/common/combobox.png
   :width: 1.5em
.. |commandlinkbutton|  image:: /static/common/commandlinkbutton.png
   :width: 1.5em
.. |dateedit|  image:: /static/common/dateedit.png
   :width: 1.5em
.. |datetimeedit|  image:: /static/common/datetimeedit.png
   :width: 1.5em
.. |dial| image:: /static/common/dial.png
   :width: 1.5em
.. |dialogbuttonbox|  image:: /static/common/dialogbuttonbox.png
   :width: 1.5em
.. |digitising|  image:: /static/common/digitising.png
   :width: 1.5em
.. |dockwidget| image:: /static/common/dockwidget.png
   :width: 1.5em
.. |doublespinbox|  image:: /static/common/doublespinbox.png
   :width: 1.5em
.. |fontcombobox|  image:: /static/common/fontcombobox.png
   :width: 1.5em
.. |frame|  image:: /static/common/frame.png
   :width: 1.5em
.. |graphicsview|  image:: /static/common/graphicsview.png
   :width: 1.5em
.. |grass_location|  image:: /static/common/grass_location.png
   :width: 1.5em
.. |groupbox|  image:: /static/common/groupbox.png
   :width: 1.5em
.. |groupboxcollapsible|  image:: /static/common/groupboxcollapsible.png
   :width: 1.5em
.. |histogram|  image:: /static/common/histogram.png
   :width: 1.5em
.. |hscrollbar|  image:: /static/common/hscrollbar.png
   :width: 1.5em
.. |hslider|  image:: /static/common/hslider.png
   :width: 1.5em
.. |hsplit|  image:: /static/common/hsplit.png
   :width: 1.5em
.. |iconAboutConsole|  image:: /static/common/iconAboutConsole.png
   :width: 1.5em
.. |iconClassBrowserConsole|  image:: /static/common/iconClassBrowserConsole.png
   :width: 1.5em
.. |iconClassConsole|  image:: /static/common/iconClassConsole.png
   :width: 1.5em
.. |iconClassTreeWidgetConsole|  image:: /static/common/iconClassTreeWidgetConsole.png
   :width: 1.5em
.. |iconClearConsole|  image:: /static/common/iconClearConsole.png
   :width: 1.5em
.. |iconCloseTabEditorConsole|  image:: /static/common/iconCloseTabEditorConsole.png
   :width: 1.5em
.. |iconCodepadConsole|  image:: /static/common/iconCodepadConsole.png
   :width: 1.5em
.. |iconCommentEditorConsole|  image:: /static/common/iconCommentEditorConsole.png
   :width: 1.5em
.. |iconCopyEditorConsole|  image:: /static/common/iconCopyEditorConsole.png
   :width: 1.5em
.. |iconCutEditorConsole|  image:: /static/common/iconCutEditorConsole.png
   :width: 1.5em
.. |iconFileTabsMenuConsole|  image:: /static/common/iconFileTabsMenuConsole.png
   :width: 1.5em
.. |iconFunctionTreeWidgetConsole|   image:: /static/common/iconFunctionTreeWidgetConsole.png
   :width: 1.5em
.. |iconHelpConsole|  image:: /static/common/iconHelpConsole.png
   :width: 1.5em
.. |iconHideToolConsole|  image:: /static/common/iconHideToolConsole.png
   :width: 1.5em
.. |iconIfaceConsole|  image:: /static/common/iconIfaceConsole.png
   :width: 1.5em
.. |iconMethodTreeWidgetConsole|  image:: /static/common/iconMethodTreeWidgetConsole.png
   :width: 1.5em
.. |iconNewTabEditorConsole|  image:: /static/common/iconNewTabEditorConsole.png
   :width: 1.5em
.. |iconOpenConsole|  image:: /static/common/iconOpenConsole.png
   :width: 1.5em
.. |iconPasteEditorConsole|  image:: /static/common/iconPasteEditorConsole.png
   :width: 1.5em
.. |iconQtCoreConsole|  image:: /static/common/iconQtCoreConsole.png
   :width: 1.5em
.. |iconQtGuiConsole|  image:: /static/common/iconQtGuiConsole.png
   :width: 1.5em
.. |iconRestoreTabsConsole|  image:: /static/common/iconRestoreTabsConsole.png
   :width: 1.5em
.. |iconRunConsole|  image:: /static/common/iconRunConsole.png
   :width: 1.5em
.. |iconRunScriptConsole|  image:: /static/common/iconRunScriptConsole.png
   :width: 1.5em
.. |iconSaveAsConsole|  image:: /static/common/iconSaveAsConsole.png
   :width: 1.5em
.. |iconSaveConsole|   image:: /static/common/iconSaveConsole.png
   :width: 1.5em
.. |iconScriptConsole|  image:: /static/common/iconScriptConsole.png
   :width: 1.5em
.. |iconSettingsConsole|  image:: /static/common/iconSettingsConsole.png
   :width: 1.5em
.. |dem_analysis| image:: /static/common/dem.png
   :width: 1.5em
.. |icon_sqlanywhere| image:: /static/common/sqlanywhere.png
   :width: 1.5em
.. |icon_dbmanager| image:: /static/common/dbmanager.png
   :width: 1.5em
.. |icon_zonal_statistics| image:: /static/common/raster-stats.png
   :width: 1.5em
.. |oracle_raster| image:: /static/common/oracle_raster.png
   :width: 1.5em
.. |raster_terrain| image:: /static/common/raster_terrain.png
   :width: 1.5em
.. |osm_load| image:: /static/common/osm_load.png
   :width: 1.5em
.. |osm_featureManager| image:: /static/common/osm_featureManager.png
   :width: 1.5em
.. |osm_download| image::  /static/common/osm_download.png
   :width: 1.5em
.. |osm_upload| image:: /static/common/osm_upload.png
   :width: 1.5em
.. |osm_import| image:: /static/common/osm_import.png
   :width: 1.5em
.. |osm_save| image:: /static/common/osm_save.png
   :width: 1.5em
.. |osm_identify| image:: /static/common/osm_identify.png
   :width: 1.5em
.. |osm_createPoint| image:: /static/common/osm_createPoint.png
   :width: 1.5em
.. |osm_createLine| image:: /static/common/osm_createLine.png
   :width: 1.5em
.. |osm_createPolygon| image:: /static/common/osm_createPolygon.png
   :width: 1.5em
.. |osm_move| image:: /static/common/osm_move.png
   :width: 1.5em
.. |osm_removeFeat| image:: /static/common/osm_removeFeat.png
   :width: 1.5em
.. |osm_removeTag| image:: /static/common/osm_removeTag.png
   :width: 1.5em
.. |osm_createRelation| image:: /static/common/osm_createRelation.png
   :width: 1.5em
.. |osm_addRelation| image:: /static/common/osm_addRelation.png
   :width: 1.5em
.. |osm_generateTags| image:: /static/common/osm_generateTags.png
   :width: 1.5em
.. |osm_editRelation| image:: /static/common/osm_editRelation.png
   :width: 1.5em
.. |osm_questionMark| image:: /static/common/osm_questionMark.png
   :width: 1.5em
.. |offline_editing_copy| image:: /static/common/offline_editing_copy.png
   :width: 1.5em
.. |interpolation| image:: /static/common/interpolation.png
   :width: 1.5em
.. |mAction| image:: /static/common/mAction.png
   :width: 1.5em
.. |mActionAddRasterLayer| image:: /static/common/mActionAddRasterLayer.png
   :width: 1.5em
.. |mActionAddOgrLayer| image:: /static/common/mActionAddOgrLayer.png
   :width: 1.5em
.. |mActionShowPluginManager| image:: /static/common/mActionShowPluginManager.png
   :width: 1.5em
.. |mActionFileNew| image:: /static/common/mActionFileNew.png
   :width: 1.5em
.. |mActionFileOpen| image:: /static/common/mActionFileOpen.png
   :width: 1.5em
.. |mActionFileSave| image:: /static/common/mActionFileSave.png
   :width: 1.5em
.. |mActionFileSaveAs| image:: /static/common/mActionFileSaveAs.png
   :width: 1.5em
.. |mActionAddImage|  image:: /static/common/mActionAddImage.png
   :width: 1.5em
.. |mActionSaveMapAsImage| image:: /static/common/mActionSaveMapAsImage.png
   :width: 1.5em
.. |mActionNewComposer| image:: /static/common/mActionNewComposer.png
   :width: 1.5em
.. |mActionComposerManager| image:: /static/common/mActionComposerManager.png
   :width: 1.5em
.. |mapserver_export| image:: /static/common/mapserver_export.png
.. |mActionExportMapServer| image:: /static/common/mActionExportMapServer.png
   :width: 1.5em
.. |mActionSaveAsSVG| image:: /static/common/mActionSaveAsSVG.png
   :width: 1.5em
.. |mActionSaveAsPDF| image:: /static/common/mActionSaveAsPDF.png
   :width: 1.5em
.. |mActionFilePrint| image:: /static/common/mActionFilePrint.png
   :width: 1.5em
.. |mActionAddArrow| image:: /static/common/mActionAddArrow.png
   :width: 1.5em
.. |mActionAddBasicShape| image:: /static/common/mActionAddBasicShape.png
   :width: 1.5em
.. |mActionAddLegend| image:: /static/common/mActionAddLegend.png
   :width: 1.5em
.. |mActionAddMap| image:: /static/common/mActionAddMap.png
   :width: 1.5em
.. |mActionLabel| image:: /static/common/mActionLabel.png
   :width: 1.5em
.. |mActionScaleBar| image:: /static/common/mActionScaleBar.png
   :width: 1.5em
.. |mActionSelectPan| image:: /static/common/mActionSelectPan.png
   :width: 1.5em
.. |mActionGroupItems| image:: /static/common/mActionGroupItems.png
   :width: 1.5em
.. |mActionUnGroupItems| image:: /static/common/mActionUngroupItems.png
   :width: 1.5em
.. |mActionRaiseItems| image:: /static/common/mActionRaiseItems.png
   :width: 1.5em
.. |mActionLowerItems| image:: /static/common/mActionLowerItems.png
   :width: 1.5em
.. |mActionMoveItemContent| image:: /static/common/mActionMoveItemContent.png
   :width: 1.5em
.. |mActionMoveItemsToTop| image:: /static/common/mActionMoveItemsToTop.png
   :width: 1.5em
.. |mActionMoveItemsToBottom| image:: /static/common/mActionMoveItemsToBottom.png
   :width: 1.5em
.. |mActionAlignLeft|  image:: /static/common/mActionAlignLeft.png
   :width: 1.5em
.. |mActionAlignRight|  image:: /static/common/mActionAlignRight.png
   :width: 1.5em
.. |mActionAlignHCenter|  image:: /static/common/mActionAlignHCenter.png
   :width: 1.5em
.. |mActionAlignVCenter|  image:: /static/common/mActionAlignVCenter.png
   :width: 1.5em
.. |mActionAlignTop|  image:: /static/common/mActionAlignTop.png
   :width: 1.5em
.. |mActionAlignBottom|  image:: /static/common/mActionAlignBottom.png
   :width: 1.5em
.. |mIconLock|  image:: /static/common/mIconLock.png
   :width: 1.5em
.. |mActionFileExit| image:: /static/common/mActionFileExit.png
.. |mActionUndo| image:: /static/common/mActionUndo.png
   :width: 1.5em
.. |mActionRedo| image:: /static/common/mActionRedo.png
   :width: 1.5em
.. |mActionSelect| image:: /static/common/mActionSelect.png
   :width: 1.5em
.. |mActionEditCut| image:: /static/common/mActionEditCut.png
   :width: 1.5em
.. |mActionEditCopy| image:: /static/common/mActionEditCopy.png
   :width: 1.5em
.. |mActionEditPaste| image:: /static/common/mActionEditPaste.png
   :width: 1.5em
.. |mActionDeleteAttribute| image:: /static/common/mActionDeleteAttribute.png
   :width: 1.5em
.. |mActionDeleteSelected| image:: /static/common/mActionDeleteSelected.png
   :width: 1.5em
.. |mActionDeleteVertex| image:: /static/common/mActionDeleteVertex.png
   :width: 1.5em
.. |mActionSimplify| image:: /static/common/mActionSimplify.png
   :width: 2em
.. |mActionAddRing| image:: /static/common/mActionAddRing.png
   :width: 2em
.. |mActionAddIsland| image:: /static/common/mActionAddIsland.png
   :width: 2em
.. |mActionDeleteRing| image:: /static/common/mActionDeleteRing.png
   :width: 2em
.. |mActionDeletePart| image:: /static/common/mActionDeletePart.png
   :width: 2em
.. |mActionReshape| image:: /static/common/mActionReshape.png
   :width: 1.5em
.. |mActionSplitFeatures| image:: /static/common/mActionSplitFeatures.png
   :width: 1.5em
.. |mActionMergeFeatures| image:: /static/common/mActionMergeFeatures.png
   :width: 1.5em
.. |mergeFeats| image:: /static/common/mActionMergeFeatures.png
   :width: 1.5em
.. |mActionNodeTool| image:: /static/common/mActionNodeTool.png
   :width: 1.5em
.. |mActionSelectedToTop| image:: /static/common/mActionSelectedToTop.png
   :width: 1.5em
.. |mActionInvertSelection| image:: /static/common/mActionInvertSelection.png
   :width: 1.5em
.. |mActionCopySelected| image:: /static/common/mActionCopySelected.png
   :width: 1.5em
.. |mActionZoomToSelected| image:: /static/common/mActionZoomToSelected.png
   :width: 1.5em
.. |mActionZoomActual| image:: /static/common/mActionZoomActual.png
   :width: 1.5em
.. |mActionNewAttribute| image:: /static/common/mActionNewAttribute.png
   :width: 1.5em
.. |mActionCalculateField| image:: /static/common/mActionCalculateField.png
   :width: 1.5em
.. |mActionRotatePointSymbols| image:: /static/common/mActionRotatePointSymbols.png
   :width: 1.5em
.. |mActionOffsetCurve| image:: /static/common/mActionOffsetCurve.png
   :width: 1.5em
.. |mActionToggleEditing| image:: /static/common/mActionToggleEditing.png
   :width: 1.5em
.. |mActionCapturePoint| image:: /static/common/mActionCapturePoint.png
   :width: 1.5em
.. |mActionCaptureLine| image:: /static/common/mActionCaptureLine.png
   :width: 1.5em
.. |mActionCapturePolygon| image:: /static/common/mActionCapturePolygon.png
   :width: 1.5em
.. |mActionMoveFeature| image:: /static/common/mActionMoveFeature.png
   :width: 1.5em
.. |mActionPan| image:: /static/common/mActionPan.png
   :width: 1.5em
.. |mActionZoomIn| image:: /static/common/mActionZoomIn.png
   :width: 1.5em
.. |mActionZoomOut| image:: /static/common/mActionZoomOut.png
   :width: 1.5em
.. |mActionIdentify| image:: /static/common/mActionIdentify.png
   :width: 1.5em
.. |mActionNewVectorLayer| image:: /static/common/mActionNewVectorLayer.png
   :width: 1.5em
.. |mActionZoomFullExtent| image:: /static/common/mActionZoomFullExtent.png
   :width: 1.5em
.. |mActionZoomToLayer| image:: /static/common/mActionZoomToLayer.png
   :width: 1.5em
.. |mActionZoomLast| image:: /static/common/mActionZoomLast.png
   :width: 1.5em
.. |mActionZoomNext| image:: /static/common/mActionZoomNext.png
   :width: 1.5em
.. |mActionMapTips| image:: /static/common/mActionMapTips.png
   :width: 1.5em
.. |mActionNewBookmark| image:: /static/common/mActionNewBookmark.png
   :width: 1.5em
.. |mActionShowBookmarks| image:: /static/common/mActionShowBookmarks.png
   :width: 1.5em
.. |mActionDraw| image:: /static/common/mActionDraw.png
   :width: 1.5em
.. |mActionAddNonDbLayer| image:: /static/common/mActionAddNonDbLayer.png
   :width: 1.5em
.. |mActionAddLayer| image:: /static/common/mActionAddLayer.png
   :width: 1.5em
.. |mActionAddSpatiaLiteLayer| image:: /static/common/mActionAddSpatiaLiteLayer.png
   :width: 1.5em
.. |mActionAddWmsLayer| image:: /static/common/mActionAddWmsLayer.png
   :width: 1.5em
.. |mActionOpenTable| image:: /static/common/mActionOpenTable.png
   :width: 1.5em
.. |mActionRemoveLayer| image:: /static/common/mActionRemoveLayer.png
   :width: 1.5em
.. |mActionLabeling| image:: /static/common/mActionLabeling.png
   :width: 1.5em
.. |mActionInOverview| image:: /static/common/mActionInOverview.png
   :width: 1.5em
.. |mActionAddAllToOverview| image:: /static/common/mActionAddAllToOverview.png
   :width: 1.5em
.. |mActionRemoveAllFromOverview| image:: /static/common/mActionRemoveAllFromOverview.png
   :width: 1.5em
.. |RemoveAllOVerview| image:: /static/common/mActionRemoveAllFromOverview.png
   :width: 1.5em
.. |mActionShowAllLayers| image:: /static/common/mActionShowAllLayers.png
   :width: 1.5em
.. |mActionHideAllLayers| image:: /static/common/mActionHideAllLayers.png
   :width: 1.5em
.. |mActionProjectProperties| image:: /static/common/mActionProjectProperties.png
   :width: 1.5em
.. |mActionCustomProjection| image:: /static/common/mActionCustomProjection.png
   :width: 1.5em
.. |mActionOptions| image:: /static/common/mActionOptions.png
   :width: 1em
.. |mActionHelpContents| image:: /static/common/mActionHelpContents.png
   :width: 1.5em
.. |mActionWhatsThis| image:: /static/common/whats_this.png
   :width: 1.5em
.. |mActionQgisHomePage| image:: /static/common/mActionQgisHomePage.png
   :width: 1.5em
.. |mActionCheckQgisVersion| image:: /static/common/mActionCheckQgisVersion.png
   :width: 1.5em
.. |mActionHelpAbout| image:: /static/common/mActionHelpAbout.png
   :width: 1.5em
.. |mActionHelpSponsors| image:: /static/common/mActionHelpSponsors.png
   :width: 1.5em
.. |mActionTextAnnotation| image:: /static/common/mActionTextAnnotation.png
   :width: 1.5em
.. |mActionAnnotation| image:: /static/common/mActionAnnotation.png
   :width: 1.5em
.. |mIconStopRendering| image:: /static/common/mIconStopRendering.png
   :width: 1.5em
.. |mIconProjectionDisabled| image:: /static/common/mIconProjectionDisabled.png
   :width: 1.5em
.. |mIconProjectionEnabled| image:: /static/common/mIconProjectionEnabled.png
   :width: 1.5em
.. |mActionMeasure| image:: /static/common/mActionMeasure.png
   :width: 1.5em
.. |mActionMeasureArea| image:: /static/common/mActionMeasureArea.png
   :width: 1.5em
.. |mActionMeasureAngle| image:: /static/common/mActionMeasureAngle.png
   :width: 1.5em
.. |spiticon| image:: /static/common/spiticon.png
.. |mActionSelectRectangle| image:: /static/common/mActionSelectRectangle.png
   :width: 1.5em
.. |mActionSelectPolygon| image:: /static/common/mActionSelectPolygon.png
   :width: 1.5em
.. |mActionSelectFreehand| image:: /static/common/mActionSelectFreehand.png
   :width: 1.5em
.. |mActionSelectRadius| image:: /static/common/mActionSelectRadius.png
   :width: 1.5em
.. |mActionDeselectAll| image:: /static/common/mActionDeselectAll.png
   :width: 1.5em
.. |mActionFormAnnotation| image:: /static/common/mActionFormAnnotation.png
   :width: 1.5em
.. |mActionContextHelp| image:: /static/common/mActionContextHelp.png
   :width: 1.5em
.. |mActionFolder| image:: /static/common/mActionFolder.png
   :width: 1.5em
.. |mIconNew| image:: /static/common/mIconNew.png
   :width: 1.5em
.. |raster-info| image:: /static/common/raster-info.png
   :width: 1.5em
.. |copyright_label| image:: /static/common/copyright_label.png
   :width: 1.5em
.. |north_arrow| image:: /static/common/north_arrow.png
   :width: 1.5em
.. |scale_bar| image:: /static/common/scale_bar.png
   :width: 2.5em
.. |plugin_installer| image:: /static/common/plugin_installer.png
   :width: 1.5em
.. |gpstrack_barchart| image:: /static/common/gpstrack_barchart.png
   :width: 1.5em
.. |gpstrack_polarchart| image:: /static/common/gpstrack_polarchart.png
   :width: 1.5em
.. |gps_importer| image:: /static/common/gps_importer.png
   :width: 1.5em
.. |wfs| image:: /static/common/wfs.png
   :width: 1.5em
.. |ftools| image:: /static/common/ftools_logo.png
   :width: 1.5em
.. |matrix| image:: /static/common/matrix.png
   :width: 1.5em
.. |sum_lines| image:: /static/common/sum_lines.png
   :width: 1.5em
.. |sum_points| image:: /static/common/sum_points.png
   :width: 1.5em
.. |unique| image:: /static/common/unique.png
   :width: 1.5em
.. |basic_statistics| image:: /static/common/basic_statistics.png
   :width: 1.5em
.. |neighbor| image:: /static/common/neighbour.png
   :width: 1.5em
.. |mean| image:: /static/common/mean.png
   :width: 1.5em
.. |intersections| image:: /static/common/intersections.png
   :width: 1.5em
.. |random_selection| image:: /static/common/random_selection.png
   :width: 1.5em
.. |sub_selection| image:: /static/common/sub_selection.png
   :width: 1.5em
.. |random_points| image:: /static/common/random_points.png
   :width: 1.5em
.. |regular_points| image:: /static/common/regular_points.png
   :width: 1.5em
.. |vector_grid| image:: /static/common/vector_grid.png
   :width: 1.5em
.. |select_location| image:: /static/common/select_location.png
   :width: 1.5em
.. |layer_extent| image:: /static/common/layer_extent.png
   :width: 1.5em
.. |convex_hull| image:: /static/common/convex_hull.png
   :width: 1.5em
.. |buffer| image:: /static/common/buffer.png
   :width: 1.5em
.. |intersect| image:: /static/common/intersect.png
   :width: 1.5em
.. |union| image:: /static/common/union.png
   :width: 1.5em
.. |sym_difference| image:: /static/common/sym_difference.png
   :width: 1.5em
.. |clip| image:: /static/common/clip.png
   :width: 1.5em
.. |difference| image:: /static/common/difference.png
   :width: 1.5em
.. |dissolve| image:: /static/common/dissolve.png
   :width: 1.5em
.. |check_geometry| image::  /static/common/check_geometry.png
   :width: 1.5em
.. |export_geometry| image:: /static/common/export_geometry.png
   :width: 1.5em
.. |centroids| image:: /static/common/centroids.png
   :width: 1.5em
.. |delaunay| image:: /static/common/delaunay.png
   :width: 1.5em
.. |simplify| image:: /static/common/simplify.png
   :width: 1.5em
.. |multi_to_single| image:: /static/common/multi_to_single.png
   :width: 1.5em
.. |single_to_multi| image:: /static/common/single_to_multi.png
   :width: 1.5em
.. |to_lines| image:: /static/common/to_lines.png
   :width: 1.5em
.. |extract_nodes| image:: /static/common/extract_nodes.png
   :width: 1.5em
.. |export_projection| image:: /static/common/export_projection.png
   :width: 1.5em
.. |define_projection| image:: /static/common/define_projection.png
   :width: 1.5em
.. |join_location| image:: /static/common/join_location.png
   :width: 1.5em
.. |split_layer| image:: /static/common/split_layer.png
   :width: 1.5em
.. |merge_shapes| image:: /static/common/merge_shapes.png
   :width: 1.5em
.. |event_browser| image:: /static/common/event_browser.png
   :width: 1.5em
.. |event_id| image:: /static/common/event_id.png
   :width: 1.5em
.. |evis_connect| image:: /static/common/evis_connect.png
   :width: 1.5em
.. |evis_file| image:: /static/common/evis_file.png
   :width: 1.5em
.. |dxf2shp_converter| image:: /static/common/dxf2shp_converter.png
   :width: 1.5em
.. |grass| image:: /static/common/grasslogo.png
   :width: 1.5em
.. |qgissplash| image:: /static/common/splash.png
.. |gentlelogo| image:: /static/common/qgislogo.png
   :width: 1.5em
.. |grass_open_mapset| image:: /static/common/grass_open_mapset.png
   :width: 1.5em
.. |grass_new_mapset| image:: /static/common/grass_new_mapset.png
   :width: 1.5em
.. |grass_close_mapset| image:: /static/common/grass_close_mapset.png
   :width: 1.5em
.. |grass_add_vector| image:: /static/common/grass_add_vector.png
   :width: 1.5em
.. |grass_add_raster| image:: /static/common/grass_add_raster.png
   :width: 1.5em
.. |grass_new_vector_layer| image:: /static/common/grass_new_vector_layer.png
   :width: 1.5em
.. |grass_edit| image:: /static/common/grass_edit.png
   :width: 1.5em
.. |grass_tools| image:: /static/common/grass_tools.png
   :width: 1.5em
.. |grass_region| image:: /static/common/grass_region.png
   :width: 1.5em
.. |grass_region_edit| image:: /static/common/grass_region_edit.png
   :width: 1.5em
.. |grass_new_point| image:: /static/common/grass_new_point.png
   :width: 1.5em
.. |grass_new_line| image:: /static/common/grass_new_line.png
   :width: 1.5em
.. |grass_new_boundary| image:: /static/common/grass_new_boundary.png
   :width: 1.5em
.. |grass_new_centroid| image:: /static/common/grass_new_centroid.png
   :width: 1.5em
.. |grass_move_vertex| image:: /static/common/grass_move_vertex.png
   :width: 1.5em
.. |grass_add_vertex| image:: /static/common/grass_add_vertex.png
   :width: 1.5em
.. |grass_delete_vertex| image:: /static/common/grass_delete_vertex.png
   :width: 1.5em
.. |grass_move_line| image:: /static/common/grass_move_line.png
   :width: 1.5em
.. |grass_split_line| image:: /static/common/grass_split_line.png
   :width: 1.5em
.. |grass_delete_line| image:: /static/common/grass_delete_line.png
   :width: 1.5em
.. |grass_edit_attributes| image:: /static/common/grass_edit_attributes.png
   :width: 1.5em
.. |grass_close_edit| image:: /static/common/grass_close_edit.png
   :width: 1.5em
.. |grass_add_map| image:: /static/common/grass_add_map.png
   :width: 1.5em
.. |grass_copy_map| image:: /static/common/grass_copy_map.png
   :width: 1.5em
.. |grass_rename_map| image:: /static/common/grass_rename_map.png
   :width: 1.5em
.. |grass_delete_map| image:: /static/common/grass_delete_map.png
   :width: 1.5em
.. |grass_set_region| image:: /static/common/grass_set_region.png
   :width: 1.5em
.. |grass_refresh| image:: /static/common/grass_refresh.png
   :width: 1.5em
.. |delimited_text| image:: /static/common/delimited_text.png
   :width: 1.5em
.. |mActionGDALScript| image:: /static/common/mActionGDALScript.png
   :width: 1.5em
.. |mActionLinkQGisToGeoref| image:: /static/common/mActionLinkQGisToGeoref.png
   :width: 2.5em
.. |mActionStartGeoref| image:: /static/common/mActionStartGeoref.png
   :width: 1.5em
.. |mActionLinkGeorefToQGis| image:: /static/common/mActionLinkGeorefToQGis.png
   :width: 2.5em
.. |georeferencer| image:: /static/common/georeferencer.png
   :width: 1.5em
.. |pencil| image:: /static/common/pencil.png
   :width: 1.5em
.. |coordinate_capture| image:: /static/common/coordinate_capture.png
   :width: 1.5em
.. |tracking| image:: /static/common/tracking.png
   :width: 1.5em
.. |plugin| image:: /static/common/plugin.png
   :width: 1.5em
.. |spatialquery| image:: /static/common/spatialquery.png
   :width: 1.5em
.. |selectesubsetlayer| image:: /static/common/selectesubsetlayer.png
   :width: 1.5em
.. |selectcreatelayer| image:: /static/common/selectcreatelayer.png
   :width: 1.5em
.. |heatmap| image:: /static/common/heatmap.png
   :width: 1.5em
.. |CRS| image:: /static/common/CRS.png
   :width: 1.5em
.. |action| image:: /static/common/action.png
   :width: 2em
.. |attributes| image:: /static/common/attributes.png
   :width: 2em
.. |diagram| image:: /static/common/diagram.png
   :width: 2em
.. |general| image:: /static/common/general.png
   :width: 2em
.. |metadata| image:: /static/common/metadata.png
   :width: 2em
.. |symbology| image:: /static/common/symbology.png
   :width: 2em
.. |join| image:: /static/common/join.png
   :width: 2em
.. |labels| image:: /static/common/labels.png
   :width: 2em
.. |locale| image:: /static/common/locale.png
   :width: 2em
.. |dbmanager| image:: /static/common/dbmanager.png
   :width: 1.5em
.. |gdal| image:: /static/common/gdal.png
   :width: 1.5em
.. |gdal_warp| image:: /static/common/warp.png
   :width: 1.5em
.. |gdal_assign_projection| image:: /static/common/projection-add.png
   :width: 1.5em
.. |gdal_extract_projection| image:: /static/common/projection-export.png
   :width: 1.5em
.. |gdal_polygonize| image:: /static/common/polygonize.png
   :width: 1.5em
.. |gdal_translate| image:: /static/common/translate.png
   :width: 1.5em
.. |gdal_dem| image:: /static/common/gdal_dem.png
   :width: 1.5em
.. |gdal_about| image:: /static/common/about.png
   :width: 1.5em
.. |gdal_contour| image:: /static/common/contour.png
   :width: 1.5em
.. |gdal_edit| image:: /static/common/edit.png
   :width: 1.5em
.. |gdal_fillnodata| image:: /static/common/fillnodata.png
   :width: 1.5em
.. |gdal_grid| image:: /static/common/grid.png
   :width: 1.5em
.. |gdal_merge| image:: /static/common/merge.png
   :width: 1.5em
.. |gdal_nearblack| image:: /static/common/nearblack.png
   :width: 1.5em
.. |gdal_proximity| image:: /static/common/proximity.png
   :width: 1.5em
.. |gdal_raster-clip| image:: /static/common/raster-clip.png
   :width: 1.5em
.. |gdal_raster-overview| image:: /static/common/raster-overview.png
   :width: 1.5em
.. |gdal_raster-paletted| image:: /static/common/raster-paletted.png
   :width: 1.5em
.. |gdal_raster-rgb| image:: /static/common/raster-rgb.png
   :width: 1.5em
.. |gdal_rasterize| image:: /static/common/rasterize.png
   :width: 1.5em
.. |gdal_reset| image:: /static/common/reset.png
   :width: 1.5em
.. |gdal_sieve| image:: /static/common/sieve.png
   :width: 1.5em
.. |gdal_tileindex| image:: /static/common/tileindex.png
   :width: 1.5em
.. |gdal_tooltip| image:: /static/common/tooltip.png
   :width: 1.5em
.. |gdal_vrt| image:: /static/common/vrt.png
   :width: 1.5em

.. |mActionAddMssqlLayer| image:: /static/common/mActionAddMssqlLayer.png
   :width: 1.5em
.. |fullCumulativeStretch| image:: /static/common/mActionFullCumulativeCutStretch.png
   :width: 1.5em
.. |FullHistogramStretch| image:: /static/common/mActionFullHistogramStretch.png
   :width: 1.5em
.. |PanToSelected| image:: /static/common/mActionPanToSelected.png
   :width: 1.5em
.. |ShowRasterCalculator| image:: /static/common/mActionShowRasterCalculator.png
   :width: 1.5em
.. |mIconZip| image:: /static/common/mIconZip.png
   :width: 2em
.. |offline_editing_sync| image:: /static/common/offline_editing_sync.png
   :width: 1.5em
.. |raster-interpolate| image:: /static/common/raster-interpolate.png
   :width: 1.5em
.. |raster-stats| image:: /static/common/raster-stats.png
   :width: 1.5em
.. |roadgraph| image:: /static/common/roadgraph.png
   :width: 1.5em
"""


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
#html_theme = 'sphinxdoc'
#html_theme = 'linfiniti-sphinx-theme'
#html_theme = 'basic'
#html_theme = 'sphinxdoc'
html_theme = 'qgis-theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['../themes']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = 'QGIS'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
html_sidebars = {
        'index': ['globaltoc.html', 'searchbox.html']
        ,'docs/**': ['localtoc.html', 'searchbox.html']
        ,'website/**': ['localtoc.html', 'searchbox.html']
#        ,'docs/gentle_gis_introduction/**': ['localtoc.html', 'searchbox.html']
#        ,'docs/pyqgis_developer_cookbook/**': ['localtoc.html', 'searchbox.html']
#        ,'docs/qgis_governance/**': ['localtoc.html', 'searchbox.html']
#        ,'docs/user_manual/**': ['localtoc.html', 'searchbox.html']
#        ,'website/**': ['localtoc.html', 'searchbox.html']
#      ,'using/windows': ['windowssidebar.html', 'sourcelink.html', 'searchbox.html']
      }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'QGISUserGuide'


# show 'build with Sphinx', defaults to True
html_show_sphinx = False

# show copyright notice, defaults to True
html_show_copyright = False

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('docs/user_manual/index', 'QGISUserGuide.tex', u'QGIS User Guide',
   u'QGIS Project', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# -- Options for PDF output ----------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author).
pdf_documents = [
    ('docs/user_manual/index', u'QGISUserGuide', u'QGIS User Guide', u'QGIS Project'),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
pdf_compressed=True

# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path=['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
# Language to be used for hyphenation support
#pdf_language="en_EN"

# If false, no index is generated.
#pdf_use_index = True

# If false, no modindex is generated.
#pdf_use_modindex = True

# If false, no coverpage is generated.
#pdf_use_coverpage = True

locale_dirs = ['../i18n']

# create 1 po file per rst file instead of one po file per module
gettext_compact = False
