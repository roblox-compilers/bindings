class Services:
    def __init__(self):
        self.AccountService = None  # type: AccountService
        self.AchievementService = None  # type: AchievementService
        self.ActivityHistoryEventService = None  # type: ActivityHistoryEventService
        self.AnalyticsService = None  # type: AnalyticsService
        self.AnimationClipProvider = None  # type: AnimationClipProvider
        self.AnimationFromVideoCreatorService = None  # type: AnimationFromVideoCreatorService
        self.AnimationFromVideoCreatorStudioService = None  # type: AnimationFromVideoCreatorStudioService
        self.AnnotationsService = None  # type: AnnotationsService
        self.AppLifecycleObserverService = None  # type: AppLifecycleObserverService
        self.AppUpdateService = None  # type: AppUpdateService
        self.AssetCounterService = None  # type: AssetCounterService
        self.AssetDeliveryProxy = None  # type: AssetDeliveryProxy
        self.AssetImportService = None  # type: AssetImportService
        self.AssetManagerService = None  # type: AssetManagerService
        self.AssetService = None  # type: AssetService
        self.AudioFocusService = None  # type: AudioFocusService
        self.AuroraScriptService = None  # type: AuroraScriptService
        self.AuroraService = None  # type: AuroraService
        self.AvatarChatService = None  # type: AvatarChatService
        self.AvatarCreationService = None  # type: AvatarCreationService
        self.AvatarEditorService = None  # type: AvatarEditorService
        self.AvatarImportService = None  # type: AvatarImportService
        self.AvatarPreloader = None  # type: AvatarPreloader
        self.AvatarSettings = None  # type: AvatarSettings
        self.BadgeService = None  # type: BadgeService
        self.BugReporterService = None  # type: BugReporterService
        self.BulkImportService = None  # type: BulkImportService
        self.CalloutService = None  # type: CalloutService
        self.CaptureService = None  # type: CaptureService
        self.ChangeHistoryService = None  # type: ChangeHistoryService
        self.Chat = None  # type: Chat
        self.ChatbotUIService = None  # type: ChatbotUIService
        self.CloudCRUDService = None  # type: CloudCRUDService
        self.CollaboratorsService = None  # type: CollaboratorsService
        self.CollectionService = None  # type: CollectionService
        self.CommandService = None  # type: CommandService
        self.CommerceService = None  # type: CommerceService
        self.ConfigService = None  # type: ConfigService
        self.ConfigureServerService = None  # type: ConfigureServerService
        self.ConnectivityService = None  # type: ConnectivityService
        self.ContentProvider = None  # type: ContentProvider
        self.ContextActionService = None  # type: ContextActionService
        self.ControllerService = None  # type: ControllerService
        self.ConversationalAIAcceptanceService = None  # type: ConversationalAIAcceptanceService
        self.CoreGui = None  # type: CoreGui
        self.CoreScriptDebuggingManagerHelper = None  # type: CoreScriptDebuggingManagerHelper
        self.CreationDBService = None  # type: CreationDBService
        self.CreatorStoreService = None  # type: CreatorStoreService
        self.CrossDMScriptChangeListener = None  # type: CrossDMScriptChangeListener
        self.DataModelPatchService = None  # type: DataModelPatchService
        self.DataStoreService = None  # type: DataStoreService
        self.Debris = None  # type: Debris
        self.DebuggablePluginWatcher = None  # type: DebuggablePluginWatcher
        self.DebuggerConnectionManager = None  # type: DebuggerConnectionManager
        self.DebuggerManager = None  # type: DebuggerManager
        self.DebuggerUIService = None  # type: DebuggerUIService
        self.DeviceIdService = None  # type: DeviceIdService
        self.DraggerService = None  # type: DraggerService
        self.EditableService = None  # type: EditableService
        self.EventIngestService = None  # type: EventIngestService
        self.ExampleService = None  # type: ExampleService
        self.ExperienceAuthService = None  # type: ExperienceAuthService
        self.ExperienceNotificationService = None  # type: ExperienceNotificationService
        self.ExperienceService = None  # type: ExperienceService
        self.ExperienceStateCaptureService = None  # type: ExperienceStateCaptureService
        self.ExplorerServiceVisibilityService = None  # type: ExplorerServiceVisibilityService
        self.FaceAnimatorService = None  # type: FaceAnimatorService
        self.FacialAgeEstimationService = None  # type: FacialAgeEstimationService
        self.FacialAnimationRecordingService = None  # type: FacialAnimationRecordingService
        self.FacialAnimationStreamingServiceV2 = None  # type: FacialAnimationStreamingServiceV2
        self.FeatureRestrictionManager = None  # type: FeatureRestrictionManager
        self.FeedService = None  # type: FeedService
        self.GamepadService = None  # type: GamepadService
        self.GamePassService = None  # type: GamePassService
        self.GenerationService = None  # type: GenerationService
        self.GenericChallengeService = None  # type: GenericChallengeService
        self.GeometryService = None  # type: GeometryService
        self.GroupService = None  # type: GroupService
        self.GuiService = None  # type: GuiService
        self.HapticService = None  # type: HapticService
        self.HeapProfilerService = None  # type: HeapProfilerService
        self.HeatmapService = None  # type: HeatmapService
        self.HeightmapImporterService = None  # type: HeightmapImporterService
        self.HttpService = None  # type: HttpService
        self.ILegacyStudioBridge = None  # type: ILegacyStudioBridge
        self.IncrementalPatchBuilder = None  # type: IncrementalPatchBuilder
        self.InsertService = None  # type: InsertService
        self.InternalSyncService = None  # type: InternalSyncService
        self.IXPService = None  # type: IXPService
        self.JointsService = None  # type: JointsService
        self.KeyframeSequenceProvider = None  # type: KeyframeSequenceProvider
        self.LanguageService = None  # type: LanguageService
        self.LegacyStudioBridge = None  # type: LegacyStudioBridge
        self.Lighting = None  # type: Lighting
        self.LinkingService = None  # type: LinkingService
        self.LiveScriptingService = None  # type: LiveScriptingService
        self.LiveSyncService = None  # type: LiveSyncService
        self.LocalizationService = None  # type: LocalizationService
        self.LodDataService = None  # type: LodDataService
        self.LogReporterService = None  # type: LogReporterService
        self.LogService = None  # type: LogService
        self.LSPFileSyncService = None  # type: LSPFileSyncService
        self.LuauScriptAnalyzerService = None  # type: LuauScriptAnalyzerService
        self.MarketplaceService = None  # type: MarketplaceService
        self.MatchmakingService = None  # type: MatchmakingService
        self.MaterialGenerationService = None  # type: MaterialGenerationService
        self.MaterialService = None  # type: MaterialService
        self.MemoryStoreService = None  # type: MemoryStoreService
        self.MessageBusService = None  # type: MessageBusService
        self.MessagingService = None  # type: MessagingService
        self.MetaBreakpointManager = None  # type: MetaBreakpointManager
        self.MLModelDeliveryService = None  # type: MLModelDeliveryService
        self.NetworkClient = None  # type: NetworkClient
        self.NetworkServer = None  # type: NetworkServer
        self.NetworkSettings = None  # type: NetworkSettings
        self.OmniRecommendationsService = None  # type: OmniRecommendationsService
        self.OpenCloudService = None  # type: OpenCloudService
        self.PackageService = None  # type: PackageService
        self.PackageUIService = None  # type: PackageUIService
        self.PatchBundlerFileWatch = None  # type: PatchBundlerFileWatch
        self.PathfindingService = None  # type: PathfindingService
        self.PerformanceControlService = None  # type: PerformanceControlService
        self.PhysicsService = None  # type: PhysicsService
        self.PlaceAssetIdsService = None  # type: PlaceAssetIdsService
        self.PlacesService = None  # type: PlacesService
        self.PlaceStatsService = None  # type: PlaceStatsService
        self.PlatformCloudStorageService = None  # type: PlatformCloudStorageService
        self.PlatformFriendsService = None  # type: PlatformFriendsService
        self.PlayerDataService = None  # type: PlayerDataService
        self.PlayerHydrationService = None  # type: PlayerHydrationService
        self.Players = None  # type: Players
        self.PlayerViewService = None  # type: PlayerViewService
        self.PluginDebugService = None  # type: PluginDebugService
        self.PluginGuiService = None  # type: PluginGuiService
        self.PluginManagementService = None  # type: PluginManagementService
        self.PluginPolicyService = None  # type: PluginPolicyService
        self.PolicyService = None  # type: PolicyService
        self.ProcessInstancePhysicsService = None  # type: ProcessInstancePhysicsService
        self.ProximityPromptService = None  # type: ProximityPromptService
        self.PublishService = None  # type: PublishService
        self.ReflectionService = None  # type: ReflectionService
        self.RemoteCursorService = None  # type: RemoteCursorService
        self.RemoteDebuggerServer = None  # type: RemoteDebuggerServer
        self.RenderSettings = None  # type: RenderSettings
        self.ReplicatedFirst = None  # type: ReplicatedFirst
        self.ReplicatedStorage = None  # type: ReplicatedStorage
        self.RibbonNotificationService = None  # type: RibbonNotificationService
        self.RobloxPluginGuiService = None  # type: RobloxPluginGuiService
        self.RobloxServerStorage = None  # type: RobloxServerStorage
        self.RomarkRbxAnalyticsService = None  # type: RomarkRbxAnalyticsService
        self.RomarkService = None  # type: RomarkService
        self.RtMessagingService = None  # type: RtMessagingService
        self.RunService = None  # type: RunService
        self.SafetyService = None  # type: SafetyService
        self.ScriptChangeService = None  # type: ScriptChangeService
        self.ScriptCloneWatcher = None  # type: ScriptCloneWatcher
        self.ScriptCloneWatcherHelper = None  # type: ScriptCloneWatcherHelper
        self.ScriptCommitService = None  # type: ScriptCommitService
        self.ScriptContext = None  # type: ScriptContext
        self.ScriptEditorService = None  # type: ScriptEditorService
        self.ScriptProfilerService = None  # type: ScriptProfilerService
        self.ScriptRegistrationService = None  # type: ScriptRegistrationService
        self.Selection = None  # type: Selection
        self.SelectionHighlightManager = None  # type: SelectionHighlightManager
        self.SerializationService = None  # type: SerializationService
        self.ServerScriptService = None  # type: ServerScriptService
        self.ServerStorage = None  # type: ServerStorage
        self.ServiceVisibilityService = None  # type: ServiceVisibilityService
        self.SessionService = None  # type: SessionService
        self.SharedTableRegistry = None  # type: SharedTableRegistry
        self.SmoothVoxelsUpgraderService = None  # type: SmoothVoxelsUpgraderService
        self.SnippetService = None  # type: SnippetService
        self.SocialService = None  # type: SocialService
        self.SoundService = None  # type: SoundService
        self.StarterGui = None  # type: StarterGui
        self.StarterPack = None  # type: StarterPack
        self.StarterPlayer = None  # type: StarterPlayer
        self.StartPageService = None  # type: StartPageService
        self.StartupMessageService = None  # type: StartupMessageService
        self.Stats = None  # type: Stats
        self.StreamingService = None  # type: StreamingService
        self.Studio = None  # type: Studio
        self.StudioAssetService = None  # type: StudioAssetService
        self.StudioCameraService = None  # type: StudioCameraService
        self.StudioData = None  # type: StudioData
        self.StudioDeviceEmulatorService = None  # type: StudioDeviceEmulatorService
        self.StudioPublishService = None  # type: StudioPublishService
        self.StudioScriptDebugEventListener = None  # type: StudioScriptDebugEventListener
        self.StudioSdkService = None  # type: StudioSdkService
        self.StudioService = None  # type: StudioService
        self.StudioUserService = None  # type: StudioUserService
        self.StudioWidgetsService = None  # type: StudioWidgetsService
        self.StylingService = None  # type: StylingService
        self.SystemThemeService = None  # type: SystemThemeService
        self.TaskScheduler = None  # type: TaskScheduler
        self.TeamCreateData = None  # type: TeamCreateData
        self.TeamCreatePublishService = None  # type: TeamCreatePublishService
        self.TeamCreateService = None  # type: TeamCreateService
        self.Teams = None  # type: Teams
        self.TelemetryService = None  # type: TelemetryService
        self.TeleportService = None  # type: TeleportService
        self.TemporaryCageMeshProvider = None  # type: TemporaryCageMeshProvider
        self.TemporaryScriptService = None  # type: TemporaryScriptService
        self.TestService = None  # type: TestService
        self.TextBoxService = None  # type: TextBoxService
        self.TextChatService = None  # type: TextChatService
        self.TextService = None  # type: TextService
        self.TextureGenerationService = None  # type: TextureGenerationService
        self.ToastNotificationService = None  # type: ToastNotificationService
        self.TracerService = None  # type: TracerService
        self.TutorialService = None  # type: TutorialService
        self.TweenService = None  # type: TweenService
        self.UGCAvatarService = None  # type: UGCAvatarService
        self.UIDragDetectorService = None  # type: UIDragDetectorService
        self.UniqueIdLookupService = None  # type: UniqueIdLookupService
        self.UnvalidatedAssetService = None  # type: UnvalidatedAssetService
        self.UserInputService = None  # type: UserInputService
        self.UserService = None  # type: UserService
        self.VersionControlService = None  # type: VersionControlService
        self.VideoCaptureService = None  # type: VideoCaptureService
        self.VideoService = None  # type: VideoService
        self.VisibilityCheckDispatcher = None  # type: VisibilityCheckDispatcher
        self.VisualizationModeService = None  # type: VisualizationModeService
        self.VoiceChatInternal = None  # type: VoiceChatInternal
        self.VoiceChatService = None  # type: VoiceChatService
        self.VRService = None  # type: VRService
        self.VRStatusService = None  # type: VRStatusService
        self.WebSocketService = None  # type: WebSocketService
        self.WebViewService = None  # type: WebViewService
        self.Workspace = None  # type: Workspace

class CreatableInstances:
    def __init__(self):
        self.Accessory = None  # type: Accessory
        self.AccessoryDescription = None  # type: AccessoryDescription
        self.Accoutrement = None  # type: Accoutrement
        self.Actor = None  # type: Actor
        self.AdGui = None  # type: AdGui
        self.AdPortal = None  # type: AdPortal
        self.AirController = None  # type: AirController
        self.AlignOrientation = None  # type: AlignOrientation
        self.AlignPosition = None  # type: AlignPosition
        self.AngularVelocity = None  # type: AngularVelocity
        self.Animation = None  # type: Animation
        self.AnimationConstraint = None  # type: AnimationConstraint
        self.AnimationController = None  # type: AnimationController
        self.AnimationRigData = None  # type: AnimationRigData
        self.Animator = None  # type: Animator
        self.Annotation = None  # type: Annotation
        self.ArcHandles = None  # type: ArcHandles
        self.Atmosphere = None  # type: Atmosphere
        self.AtmosphereSensor = None  # type: AtmosphereSensor
        self.Attachment = None  # type: Attachment
        self.AudioAnalyzer = None  # type: AudioAnalyzer
        self.AudioChannelMixer = None  # type: AudioChannelMixer
        self.AudioChannelSplitter = None  # type: AudioChannelSplitter
        self.AudioChorus = None  # type: AudioChorus
        self.AudioCompressor = None  # type: AudioCompressor
        self.AudioDeviceInput = None  # type: AudioDeviceInput
        self.AudioDeviceOutput = None  # type: AudioDeviceOutput
        self.AudioDistortion = None  # type: AudioDistortion
        self.AudioEcho = None  # type: AudioEcho
        self.AudioEmitter = None  # type: AudioEmitter
        self.AudioEqualizer = None  # type: AudioEqualizer
        self.AudioFader = None  # type: AudioFader
        self.AudioFilter = None  # type: AudioFilter
        self.AudioFlanger = None  # type: AudioFlanger
        self.AudioLimiter = None  # type: AudioLimiter
        self.AudioListener = None  # type: AudioListener
        self.AudioPitchShifter = None  # type: AudioPitchShifter
        self.AudioPlayer = None  # type: AudioPlayer
        self.AudioRecorder = None  # type: AudioRecorder
        self.AudioReverb = None  # type: AudioReverb
        self.AudioSearchParams = None  # type: AudioSearchParams
        self.AudioTextToSpeech = None  # type: AudioTextToSpeech
        self.AuroraScript = None  # type: AuroraScript
        self.AvatarAccessoryRules = None  # type: AvatarAccessoryRules
        self.AvatarAnimationRules = None  # type: AvatarAnimationRules
        self.AvatarBodyRules = None  # type: AvatarBodyRules
        self.AvatarClothingRules = None  # type: AvatarClothingRules
        self.AvatarCollisionRules = None  # type: AvatarCollisionRules
        self.AvatarRules = None  # type: AvatarRules
        self.Backpack = None  # type: Backpack
        self.BallSocketConstraint = None  # type: BallSocketConstraint
        self.Beam = None  # type: Beam
        self.BillboardGui = None  # type: BillboardGui
        self.BindableEvent = None  # type: BindableEvent
        self.BindableFunction = None  # type: BindableFunction
        self.BlockMesh = None  # type: BlockMesh
        self.BloomEffect = None  # type: BloomEffect
        self.BlurEffect = None  # type: BlurEffect
        self.BodyAngularVelocity = None  # type: BodyAngularVelocity
        self.BodyColors = None  # type: BodyColors
        self.BodyForce = None  # type: BodyForce
        self.BodyGyro = None  # type: BodyGyro
        self.BodyPartDescription = None  # type: BodyPartDescription
        self.BodyPosition = None  # type: BodyPosition
        self.BodyThrust = None  # type: BodyThrust
        self.BodyVelocity = None  # type: BodyVelocity
        self.Bone = None  # type: Bone
        self.BoolValue = None  # type: BoolValue
        self.BoxHandleAdornment = None  # type: BoxHandleAdornment
        self.Breakpoint = None  # type: Breakpoint
        self.BrickColorValue = None  # type: BrickColorValue
        self.BubbleChatMessageProperties = None  # type: BubbleChatMessageProperties
        self.BuoyancySensor = None  # type: BuoyancySensor
        self.Camera = None  # type: Camera
        self.CanvasGroup = None  # type: CanvasGroup
        self.CFrameValue = None  # type: CFrameValue
        self.CharacterMesh = None  # type: CharacterMesh
        self.ChorusSoundEffect = None  # type: ChorusSoundEffect
        self.ClickDetector = None  # type: ClickDetector
        self.ClimbController = None  # type: ClimbController
        self.Clouds = None  # type: Clouds
        self.Color3Value = None  # type: Color3Value
        self.ColorCorrectionEffect = None  # type: ColorCorrectionEffect
        self.ColorGradingEffect = None  # type: ColorGradingEffect
        self.CompressorSoundEffect = None  # type: CompressorSoundEffect
        self.ConeHandleAdornment = None  # type: ConeHandleAdornment
        self.Configuration = None  # type: Configuration
        self.ControllerManager = None  # type: ControllerManager
        self.ControllerPartSensor = None  # type: ControllerPartSensor
        self.CornerWedgePart = None  # type: CornerWedgePart
        self.CurveAnimation = None  # type: CurveAnimation
        self.CustomLog = None  # type: CustomLog
        self.CylinderHandleAdornment = None  # type: CylinderHandleAdornment
        self.CylinderMesh = None  # type: CylinderMesh
        self.CylindricalConstraint = None  # type: CylindricalConstraint
        self.DataStoreGetOptions = None  # type: DataStoreGetOptions
        self.DataStoreIncrementOptions = None  # type: DataStoreIncrementOptions
        self.DataStoreOptions = None  # type: DataStoreOptions
        self.DataStoreSetOptions = None  # type: DataStoreSetOptions
        self.Decal = None  # type: Decal
        self.DepthOfFieldEffect = None  # type: DepthOfFieldEffect
        self.Dialog = None  # type: Dialog
        self.DialogChoice = None  # type: DialogChoice
        self.DistortionSoundEffect = None  # type: DistortionSoundEffect
        self.DoubleConstrainedValue = None  # type: DoubleConstrainedValue
        self.DragDetector = None  # type: DragDetector
        self.Dragger = None  # type: Dragger
        self.EchoSoundEffect = None  # type: EchoSoundEffect
        self.EqualizerSoundEffect = None  # type: EqualizerSoundEffect
        self.EulerRotationCurve = None  # type: EulerRotationCurve
        self.ExperienceInviteOptions = None  # type: ExperienceInviteOptions
        self.ExplorerFilter = None  # type: ExplorerFilter
        self.Explosion = None  # type: Explosion
        self.FaceControls = None  # type: FaceControls
        self.FileMesh = None  # type: FileMesh
        self.Fire = None  # type: Fire
        self.FlangeSoundEffect = None  # type: FlangeSoundEffect
        self.FloatCurve = None  # type: FloatCurve
        self.FloorWire = None  # type: FloorWire
        self.FluidForceSensor = None  # type: FluidForceSensor
        self.Folder = None  # type: Folder
        self.ForceField = None  # type: ForceField
        self.Frame = None  # type: Frame
        self.GetTextBoundsParams = None  # type: GetTextBoundsParams
        self.Glue = None  # type: Glue
        self.GroundController = None  # type: GroundController
        self.Handles = None  # type: Handles
        self.HandRigDescription = None  # type: HandRigDescription
        self.HapticEffect = None  # type: HapticEffect
        self.Hat = None  # type: Hat
        self.HiddenSurfaceRemovalAsset = None  # type: HiddenSurfaceRemovalAsset
        self.Highlight = None  # type: Highlight
        self.HingeConstraint = None  # type: HingeConstraint
        self.Hole = None  # type: Hole
        self.Humanoid = None  # type: Humanoid
        self.HumanoidController = None  # type: HumanoidController
        self.HumanoidDescription = None  # type: HumanoidDescription
        self.HumanoidRigDescription = None  # type: HumanoidRigDescription
        self.IKControl = None  # type: IKControl
        self.ImageButton = None  # type: ImageButton
        self.ImageHandleAdornment = None  # type: ImageHandleAdornment
        self.ImageLabel = None  # type: ImageLabel
        self.InputAction = None  # type: InputAction
        self.InputBinding = None  # type: InputBinding
        self.InputContext = None  # type: InputContext
        self.IntConstrainedValue = None  # type: IntConstrainedValue
        self.InternalSyncItem = None  # type: InternalSyncItem
        self.IntersectOperation = None  # type: IntersectOperation
        self.IntValue = None  # type: IntValue
        self.Keyframe = None  # type: Keyframe
        self.KeyframeMarker = None  # type: KeyframeMarker
        self.KeyframeSequence = None  # type: KeyframeSequence
        self.LinearVelocity = None  # type: LinearVelocity
        self.LineForce = None  # type: LineForce
        self.LineHandleAdornment = None  # type: LineHandleAdornment
        self.LocalizationTable = None  # type: LocalizationTable
        self.LocalScript = None  # type: LocalScript
        self.ManualGlue = None  # type: ManualGlue
        self.ManualWeld = None  # type: ManualWeld
        self.MarkerCurve = None  # type: MarkerCurve
        self.MaterialVariant = None  # type: MaterialVariant
        self.MeshPart = None  # type: MeshPart
        self.Model = None  # type: Model
        self.ModuleScript = None  # type: ModuleScript
        self.Motor = None  # type: Motor
        self.Motor6D = None  # type: Motor6D
        self.MotorFeature = None  # type: MotorFeature
        self.NegateOperation = None  # type: NegateOperation
        self.NoCollisionConstraint = None  # type: NoCollisionConstraint
        self.Noise = None  # type: Noise
        self.NumberPose = None  # type: NumberPose
        self.NumberValue = None  # type: NumberValue
        self.ObjectValue = None  # type: ObjectValue
        self.OperationGraph = None  # type: OperationGraph
        self.Pants = None  # type: Pants
        self.Part = None  # type: Part
        self.ParticleEmitter = None  # type: ParticleEmitter
        self.PartOperation = None  # type: PartOperation
        self.Path2D = None  # type: Path2D
        self.PathfindingLink = None  # type: PathfindingLink
        self.PathfindingModifier = None  # type: PathfindingModifier
        self.PitchShiftSoundEffect = None  # type: PitchShiftSoundEffect
        self.Plane = None  # type: Plane
        self.PlaneConstraint = None  # type: PlaneConstraint
        self.PluginAction = None  # type: PluginAction
        self.PluginCapabilities = None  # type: PluginCapabilities
        self.PointLight = None  # type: PointLight
        self.Pose = None  # type: Pose
        self.PrismaticConstraint = None  # type: PrismaticConstraint
        self.ProximityPrompt = None  # type: ProximityPrompt
        self.RayValue = None  # type: RayValue
        self.RelativeGui = None  # type: RelativeGui
        self.RemoteEvent = None  # type: RemoteEvent
        self.RemoteFunction = None  # type: RemoteFunction
        self.RenderingTest = None  # type: RenderingTest
        self.ReverbSoundEffect = None  # type: ReverbSoundEffect
        self.RigidConstraint = None  # type: RigidConstraint
        self.RocketPropulsion = None  # type: RocketPropulsion
        self.RodConstraint = None  # type: RodConstraint
        self.RopeConstraint = None  # type: RopeConstraint
        self.Rotate = None  # type: Rotate
        self.RotateP = None  # type: RotateP
        self.RotateV = None  # type: RotateV
        self.RotationCurve = None  # type: RotationCurve
        self.RTAnimationTracker = None  # type: RTAnimationTracker
        self.ScreenGui = None  # type: ScreenGui
        self.Script = None  # type: Script
        self.ScrollingFrame = None  # type: ScrollingFrame
        self.Seat = None  # type: Seat
        self.SelectionBox = None  # type: SelectionBox
        self.SelectionPartLasso = None  # type: SelectionPartLasso
        self.SelectionPointLasso = None  # type: SelectionPointLasso
        self.SelectionSphere = None  # type: SelectionSphere
        self.Shirt = None  # type: Shirt
        self.ShirtGraphic = None  # type: ShirtGraphic
        self.SkateboardController = None  # type: SkateboardController
        self.SkateboardPlatform = None  # type: SkateboardPlatform
        self.Sky = None  # type: Sky
        self.Smoke = None  # type: Smoke
        self.Snap = None  # type: Snap
        self.Sound = None  # type: Sound
        self.SoundGroup = None  # type: SoundGroup
        self.Sparkles = None  # type: Sparkles
        self.SpawnLocation = None  # type: SpawnLocation
        self.SpecialMesh = None  # type: SpecialMesh
        self.SphereHandleAdornment = None  # type: SphereHandleAdornment
        self.SpotLight = None  # type: SpotLight
        self.SpringConstraint = None  # type: SpringConstraint
        self.StarterGear = None  # type: StarterGear
        self.StringValue = None  # type: StringValue
        self.StudioAttachment = None  # type: StudioAttachment
        self.StudioCallout = None  # type: StudioCallout
        self.StyleDerive = None  # type: StyleDerive
        self.StyleLink = None  # type: StyleLink
        self.StyleRule = None  # type: StyleRule
        self.StyleSheet = None  # type: StyleSheet
        self.SunRaysEffect = None  # type: SunRaysEffect
        self.SurfaceAppearance = None  # type: SurfaceAppearance
        self.SurfaceGui = None  # type: SurfaceGui
        self.SurfaceLight = None  # type: SurfaceLight
        self.SurfaceSelection = None  # type: SurfaceSelection
        self.SwimController = None  # type: SwimController
        self.Team = None  # type: Team
        self.TeleportOptions = None  # type: TeleportOptions
        self.TerrainDetail = None  # type: TerrainDetail
        self.TerrainRegion = None  # type: TerrainRegion
        self.TextBox = None  # type: TextBox
        self.TextButton = None  # type: TextButton
        self.TextChannel = None  # type: TextChannel
        self.TextChatCommand = None  # type: TextChatCommand
        self.TextChatMessageProperties = None  # type: TextChatMessageProperties
        self.TextLabel = None  # type: TextLabel
        self.Texture = None  # type: Texture
        self.Tool = None  # type: Tool
        self.Torque = None  # type: Torque
        self.TorsionSpringConstraint = None  # type: TorsionSpringConstraint
        self.TrackerStreamAnimation = None  # type: TrackerStreamAnimation
        self.Trail = None  # type: Trail
        self.TremoloSoundEffect = None  # type: TremoloSoundEffect
        self.TrussPart = None  # type: TrussPart
        self.UIAspectRatioConstraint = None  # type: UIAspectRatioConstraint
        self.UICorner = None  # type: UICorner
        self.UIDragDetector = None  # type: UIDragDetector
        self.UIFlexItem = None  # type: UIFlexItem
        self.UIGradient = None  # type: UIGradient
        self.UIGridLayout = None  # type: UIGridLayout
        self.UIListLayout = None  # type: UIListLayout
        self.UIPadding = None  # type: UIPadding
        self.UIPageLayout = None  # type: UIPageLayout
        self.UIScale = None  # type: UIScale
        self.UISizeConstraint = None  # type: UISizeConstraint
        self.UIStroke = None  # type: UIStroke
        self.UITableLayout = None  # type: UITableLayout
        self.UITextSizeConstraint = None  # type: UITextSizeConstraint
        self.UnionOperation = None  # type: UnionOperation
        self.UniversalConstraint = None  # type: UniversalConstraint
        self.UnreliableRemoteEvent = None  # type: UnreliableRemoteEvent
        self.Vector3Curve = None  # type: Vector3Curve
        self.Vector3Value = None  # type: Vector3Value
        self.VectorForce = None  # type: VectorForce
        self.VehicleController = None  # type: VehicleController
        self.VehicleSeat = None  # type: VehicleSeat
        self.VelocityMotor = None  # type: VelocityMotor
        self.VideoDeviceInput = None  # type: VideoDeviceInput
        self.VideoDisplay = None  # type: VideoDisplay
        self.VideoFrame = None  # type: VideoFrame
        self.VideoPlayer = None  # type: VideoPlayer
        self.ViewportFrame = None  # type: ViewportFrame
        self.VisualizationMode = None  # type: VisualizationMode
        self.VisualizationModeCategory = None  # type: VisualizationModeCategory
        self.WedgePart = None  # type: WedgePart
        self.Weld = None  # type: Weld
        self.WeldConstraint = None  # type: WeldConstraint
        self.Wire = None  # type: Wire
        self.WireframeHandleAdornment = None  # type: WireframeHandleAdornment
        self.WorkspaceAnnotation = None  # type: WorkspaceAnnotation
        self.WorldModel = None  # type: WorldModel
        self.WrapDeformer = None  # type: WrapDeformer
        self.WrapLayer = None  # type: WrapLayer
        self.WrapTarget = None  # type: WrapTarget

class Instances:
    def __init__(self):
        self.AnimationClip = None  # type: AnimationClip
        self.AnimationImportData = None  # type: AnimationImportData
        self.AnimationStreamTrack = None  # type: AnimationStreamTrack
        self.AnimationTrack = None  # type: AnimationTrack
        self.AssetImportSession = None  # type: AssetImportSession
        self.AssetPatchSettings = None  # type: AssetPatchSettings
        self.AssetSoundEffect = None  # type: AssetSoundEffect
        self.AudioPages = None  # type: AudioPages
        self.AuroraScriptObject = None  # type: AuroraScriptObject
        self.BackpackItem = None  # type: BackpackItem
        self.BanHistoryPages = None  # type: BanHistoryPages
        self.BaseImportData = None  # type: BaseImportData
        self.BasePart = None  # type: BasePart
        self.BasePlayerGui = None  # type: BasePlayerGui
        self.BaseRemoteEvent = None  # type: BaseRemoteEvent
        self.BaseScript = None  # type: BaseScript
        self.BaseWrap = None  # type: BaseWrap
        self.BevelMesh = None  # type: BevelMesh
        self.BodyMover = None  # type: BodyMover
        self.BubbleChatConfiguration = None  # type: BubbleChatConfiguration
        self.CatalogPages = None  # type: CatalogPages
        self.ChannelSelectorSoundEffect = None  # type: ChannelSelectorSoundEffect
        self.ChannelTabsConfiguration = None  # type: ChannelTabsConfiguration
        self.CharacterAppearance = None  # type: CharacterAppearance
        self.ChatInputBarConfiguration = None  # type: ChatInputBarConfiguration
        self.ChatWindowConfiguration = None  # type: ChatWindowConfiguration
        self.ChatWindowMessageProperties = None  # type: ChatWindowMessageProperties
        self.ClientReplicator = None  # type: ClientReplicator
        self.Clothing = None  # type: Clothing
        self.CloudLocalizationTable = None  # type: CloudLocalizationTable
        self.Collaborator = None  # type: Collaborator
        self.CommandInstance = None  # type: CommandInstance
        self.Constraint = None  # type: Constraint
        self.Controller = None  # type: Controller
        self.ControllerBase = None  # type: ControllerBase
        self.ControllerSensor = None  # type: ControllerSensor
        self.CustomSoundEffect = None  # type: CustomSoundEffect
        self.DataModel = None  # type: DataModel
        self.DataModelMesh = None  # type: DataModelMesh
        self.DataModelSession = None  # type: DataModelSession
        self.DataStore = None  # type: DataStore
        self.DataStoreInfo = None  # type: DataStoreInfo
        self.DataStoreKey = None  # type: DataStoreKey
        self.DataStoreKeyInfo = None  # type: DataStoreKeyInfo
        self.DataStoreKeyPages = None  # type: DataStoreKeyPages
        self.DataStoreListingPages = None  # type: DataStoreListingPages
        self.DataStoreObjectVersionInfo = None  # type: DataStoreObjectVersionInfo
        self.DataStorePages = None  # type: DataStorePages
        self.DataStoreVersionPages = None  # type: DataStoreVersionPages
        self.DebuggerBreakpoint = None  # type: DebuggerBreakpoint
        self.DebuggerConnection = None  # type: DebuggerConnection
        self.DebuggerLuaResponse = None  # type: DebuggerLuaResponse
        self.DebuggerVariable = None  # type: DebuggerVariable
        self.DebuggerWatch = None  # type: DebuggerWatch
        self.DebugSettings = None  # type: DebugSettings
        self.DockWidgetPluginGui = None  # type: DockWidgetPluginGui
        self.DynamicRotate = None  # type: DynamicRotate
        self.EmotesPages = None  # type: EmotesPages
        self.ExplorerFilterAutocompleter = None  # type: ExplorerFilterAutocompleter
        self.FaceInstance = None  # type: FaceInstance
        self.FacialAnimationStreamingServiceStats = None  # type: FacialAnimationStreamingServiceStats
        self.FacialAnimationStreamingSubsessionStats = None  # type: FacialAnimationStreamingSubsessionStats
        self.FacsImportData = None  # type: FacsImportData
        self.Feature = None  # type: Feature
        self.FeedPages = None  # type: FeedPages
        self.File = None  # type: File
        self.FormFactorPart = None  # type: FormFactorPart
        self.FriendPages = None  # type: FriendPages
        self.GameSettings = None  # type: GameSettings
        self.GenericSettings = None  # type: GenericSettings
        self.GlobalDataStore = None  # type: GlobalDataStore
        self.GlobalSettings = None  # type: GlobalSettings
        self.GroupImportData = None  # type: GroupImportData
        self.GuiBase = None  # type: GuiBase
        self.GuiBase2d = None  # type: GuiBase2d
        self.GuiBase3d = None  # type: GuiBase3d
        self.GuiButton = None  # type: GuiButton
        self.GuiLabel = None  # type: GuiLabel
        self.GuiObject = None  # type: GuiObject
        self.HandleAdornment = None  # type: HandleAdornment
        self.HandlesBase = None  # type: HandlesBase
        self.ImportSession = None  # type: ImportSession
        self.InputObject = None  # type: InputObject
        self.Instance = None  # type: Instance
        self.InstanceAdornment = None  # type: InstanceAdornment
        self.InventoryPages = None  # type: InventoryPages
        self.JointImportData = None  # type: JointImportData
        self.JointInstance = None  # type: JointInstance
        self.LayerCollector = None  # type: LayerCollector
        self.Light = None  # type: Light
        self.LocalDebuggerConnection = None  # type: LocalDebuggerConnection
        self.LodDataEntity = None  # type: LodDataEntity
        self.LuaSettings = None  # type: LuaSettings
        self.LuaSourceContainer = None  # type: LuaSourceContainer
        self.ManualSurfaceJointInstance = None  # type: ManualSurfaceJointInstance
        self.MaterialGenerationSession = None  # type: MaterialGenerationSession
        self.MaterialImportData = None  # type: MaterialImportData
        self.MemoryStoreHashMap = None  # type: MemoryStoreHashMap
        self.MemoryStoreHashMapPages = None  # type: MemoryStoreHashMapPages
        self.MemoryStoreQueue = None  # type: MemoryStoreQueue
        self.MemoryStoreSortedMap = None  # type: MemoryStoreSortedMap
        self.MemStorageConnection = None  # type: MemStorageConnection
        self.MeshImportData = None  # type: MeshImportData
        self.MessageBusConnection = None  # type: MessageBusConnection
        self.MetaBreakpoint = None  # type: MetaBreakpoint
        self.MetaBreakpointContext = None  # type: MetaBreakpointContext
        self.Mouse = None  # type: Mouse
        self.MultipleDocumentInterfaceInstance = None  # type: MultipleDocumentInterfaceInstance
        self.NetworkMarker = None  # type: NetworkMarker
        self.NetworkPeer = None  # type: NetworkPeer
        self.NetworkReplicator = None  # type: NetworkReplicator
        self.OpenCloudApiV1 = None  # type: OpenCloudApiV1
        self.OrderedDataStore = None  # type: OrderedDataStore
        self.OutfitPages = None  # type: OutfitPages
        self.PackageLink = None  # type: PackageLink
        self.Pages = None  # type: Pages
        self.ParabolaAdornment = None  # type: ParabolaAdornment
        self.PartAdornment = None  # type: PartAdornment
        self.PatchMapping = None  # type: PatchMapping
        self.Path = None  # type: Path
        self.PausedState = None  # type: PausedState
        self.PausedStateBreakpoint = None  # type: PausedStateBreakpoint
        self.PausedStateException = None  # type: PausedStateException
        self.PhysicsSettings = None  # type: PhysicsSettings
        self.Platform = None  # type: Platform
        self.Player = None  # type: Player
        self.PlayerData = None  # type: PlayerData
        self.PlayerDataRecord = None  # type: PlayerDataRecord
        self.PlayerDataRecordConfig = None  # type: PlayerDataRecordConfig
        self.PlayerGui = None  # type: PlayerGui
        self.PlayerMouse = None  # type: PlayerMouse
        self.PlayerScripts = None  # type: PlayerScripts
        self.Plugin = None  # type: Plugin
        self.PluginDragEvent = None  # type: PluginDragEvent
        self.PluginGui = None  # type: PluginGui
        self.PluginManagerInterface = None  # type: PluginManagerInterface
        self.PluginMenu = None  # type: PluginMenu
        self.PluginMouse = None  # type: PluginMouse
        self.PluginToolbar = None  # type: PluginToolbar
        self.PluginToolbarButton = None  # type: PluginToolbarButton
        self.PoseBase = None  # type: PoseBase
        self.PostEffect = None  # type: PostEffect
        self.PVAdornment = None  # type: PVAdornment
        self.PVInstance = None  # type: PVInstance
        self.QWidgetPluginGui = None  # type: QWidgetPluginGui
        self.RobloxSerializableInstance = None  # type: RobloxSerializableInstance
        self.RootImportData = None  # type: RootImportData
        self.RunningAverageItemDouble = None  # type: RunningAverageItemDouble
        self.RunningAverageItemInt = None  # type: RunningAverageItemInt
        self.RunningAverageTimeIntervalItem = None  # type: RunningAverageTimeIntervalItem
        self.ScreenshotHud = None  # type: ScreenshotHud
        self.ScriptBuilder = None  # type: ScriptBuilder
        self.ScriptDebugger = None  # type: ScriptDebugger
        self.ScriptDocument = None  # type: ScriptDocument
        self.ScriptRuntime = None  # type: ScriptRuntime
        self.SelectionLasso = None  # type: SelectionLasso
        self.SensorBase = None  # type: SensorBase
        self.ServerReplicator = None  # type: ServerReplicator
        self.ServiceProvider = None  # type: ServiceProvider
        self.SlidingBallConstraint = None  # type: SlidingBallConstraint
        self.SoundEffect = None  # type: SoundEffect
        self.StackFrame = None  # type: StackFrame
        self.StandardPages = None  # type: StandardPages
        self.StarterCharacterScripts = None  # type: StarterCharacterScripts
        self.StarterPlayerScripts = None  # type: StarterPlayerScripts
        self.StatsItem = None  # type: StatsItem
        self.StudioObjectBase = None  # type: StudioObjectBase
        self.StudioTheme = None  # type: StudioTheme
        self.StudioWidget = None  # type: StudioWidget
        self.StyleBase = None  # type: StyleBase
        self.SurfaceGuiBase = None  # type: SurfaceGuiBase
        self.SyncScriptBuilder = None  # type: SyncScriptBuilder
        self.TeleportAsyncResult = None  # type: TeleportAsyncResult
        self.Terrain = None  # type: Terrain
        self.TextChatConfigurations = None  # type: TextChatConfigurations
        self.TextChatMessage = None  # type: TextChatMessage
        self.TextFilterResult = None  # type: TextFilterResult
        self.TextFilterTranslatedResult = None  # type: TextFilterTranslatedResult
        self.TextSource = None  # type: TextSource
        self.TextureGenerationPartGroup = None  # type: TextureGenerationPartGroup
        self.TextureGenerationUnwrappingRequest = None  # type: TextureGenerationUnwrappingRequest
        self.ThreadState = None  # type: ThreadState
        self.TotalCountTimeIntervalItem = None  # type: TotalCountTimeIntervalItem
        self.TouchTransmitter = None  # type: TouchTransmitter
        self.TrackerLodController = None  # type: TrackerLodController
        self.Translator = None  # type: Translator
        self.TriangleMeshPart = None  # type: TriangleMeshPart
        self.Tween = None  # type: Tween
        self.TweenBase = None  # type: TweenBase
        self.UIBase = None  # type: UIBase
        self.UIComponent = None  # type: UIComponent
        self.UIConstraint = None  # type: UIConstraint
        self.UIGridStyleLayout = None  # type: UIGridStyleLayout
        self.UILayout = None  # type: UILayout
        self.UserGameSettings = None  # type: UserGameSettings
        self.UserSettings = None  # type: UserSettings
        self.ValueBase = None  # type: ValueBase
        self.WebSocketClient = None  # type: WebSocketClient
        self.WorldRoot = None  # type: WorldRoot

class Objects:
    def __init__(self):
        self.Capture = None  # type: Capture
        self.ConfigSnapshot = None  # type: ConfigSnapshot
        self.EditableImage = None  # type: EditableImage
        self.EditableMesh = None  # type: EditableMesh
        self.Object = None  # type: RBXObject
        self.ScreenshotCapture = None  # type: ScreenshotCapture
        self.VideoCapture = None  # type: VideoCapture

class RBXObject:
    def __init__(self):
        self._nominal_Object = None  # type: unique symbol

class Capture:
    def __init__(self):
        self._nominal_Capture = None  # type: unique symbol

class ScreenshotCapture:
    def __init__(self):
        self._nominal_ScreenshotCapture = None  # type: unique symbol

class VideoCapture:
    def __init__(self):
        self._nominal_VideoCapture = None  # type: unique symbol

class ConfigSnapshot:
    def __init__(self):
        self._nominal_ConfigSnapshot = None  # type: unique symbol

class EditableImage:
    def __init__(self):
        self._nominal_EditableImage = None  # type: unique symbol

class EditableMesh:
    def __init__(self):
        self._nominal_EditableMesh = None  # type: unique symbol

class Instance:
    def __init__(self):
        self._nominal_Instance = None  # type: unique symbol
        self.RobloxLocked = None  # type: bool

class AccessoryDescription:
    def __init__(self):
        self._nominal_AccessoryDescription = None  # type: unique symbol

class AccountService:
    def __init__(self):
        self._nominal_AccountService = None  # type: unique symbol

class Accoutrement:
    def __init__(self):
        self._nominal_Accoutrement = None  # type: unique symbol

class Accessory:
    def __init__(self):
        self._nominal_Accessory = None  # type: unique symbol

class Hat:
    def __init__(self):
        self._nominal_Hat = None  # type: unique symbol

class AchievementService:
    def __init__(self):
        self._nominal_AchievementService = None  # type: unique symbol

class ActivityHistoryEventService:
    def __init__(self):
        self._nominal_ActivityHistoryEventService = None  # type: unique symbol

class AdPortal:
    def __init__(self):
        self._nominal_AdPortal = None  # type: unique symbol

class AnalyticsService:
    def __init__(self):
        self._nominal_AnalyticsService = None  # type: unique symbol

class Animation:
    def __init__(self):
        self._nominal_Animation = None  # type: unique symbol

class AnimationClip:
    def __init__(self):
        self._nominal_AnimationClip = None  # type: unique symbol

class CurveAnimation:
    def __init__(self):
        self._nominal_CurveAnimation = None  # type: unique symbol

class KeyframeSequence:
    def __init__(self):
        self._nominal_KeyframeSequence = None  # type: unique symbol
        self.AuthoredHipHeight = None  # type: float

class AnimationClipProvider:
    def __init__(self):
        self._nominal_AnimationClipProvider = None  # type: unique symbol

class AnimationController:
    def __init__(self):
        self._nominal_AnimationController = None  # type: unique symbol

class AnimationFromVideoCreatorService:
    def __init__(self):
        self._nominal_AnimationFromVideoCreatorService = None  # type: unique symbol

class AnimationFromVideoCreatorStudioService:
    def __init__(self):
        self._nominal_AnimationFromVideoCreatorStudioService = None  # type: unique symbol

class AnimationRigData:
    def __init__(self):
        self._nominal_AnimationRigData = None  # type: unique symbol

class AnimationStreamTrack:
    def __init__(self):
        self._nominal_AnimationStreamTrack = None  # type: unique symbol

class AnimationTrack:
    def __init__(self):
        self._nominal_AnimationTrack = None  # type: unique symbol

class Animator:
    def __init__(self):
        self._nominal_Animator = None  # type: unique symbol

class Annotation:
    def __init__(self):
        self._nominal_Annotation = None  # type: unique symbol

class WorkspaceAnnotation:
    def __init__(self):
        self._nominal_WorkspaceAnnotation = None  # type: unique symbol

class AnnotationsService:
    def __init__(self):
        self._nominal_AnnotationsService = None  # type: unique symbol

class AppLifecycleObserverService:
    def __init__(self):
        self._nominal_AppLifecycleObserverService = None  # type: unique symbol

class AppUpdateService:
    def __init__(self):
        self._nominal_AppUpdateService = None  # type: unique symbol

class AssetCounterService:
    def __init__(self):
        self._nominal_AssetCounterService = None  # type: unique symbol

class AssetDeliveryProxy:
    def __init__(self):
        self._nominal_AssetDeliveryProxy = None  # type: unique symbol

class AssetImportService:
    def __init__(self):
        self._nominal_AssetImportService = None  # type: unique symbol

class AssetManagerService:
    def __init__(self):
        self._nominal_AssetManagerService = None  # type: unique symbol

class AssetPatchSettings:
    def __init__(self):
        self._nominal_AssetPatchSettings = None  # type: unique symbol

class AssetService:
    def __init__(self):
        self._nominal_AssetService = None  # type: unique symbol

class Atmosphere:
    def __init__(self):
        self._nominal_Atmosphere = None  # type: unique symbol

class Attachment:
    def __init__(self):
        self._nominal_Attachment = None  # type: unique symbol

class Bone:
    def __init__(self):
        self._nominal_Bone = None  # type: unique symbol

class AudioAnalyzer:
    def __init__(self):
        self._nominal_AudioAnalyzer = None  # type: unique symbol

class AudioChannelMixer:
    def __init__(self):
        self._nominal_AudioChannelMixer = None  # type: unique symbol

class AudioChannelSplitter:
    def __init__(self):
        self._nominal_AudioChannelSplitter = None  # type: unique symbol

class AudioChorus:
    def __init__(self):
        self._nominal_AudioChorus = None  # type: unique symbol

class AudioCompressor:
    def __init__(self):
        self._nominal_AudioCompressor = None  # type: unique symbol

class AudioDeviceInput:
    def __init__(self):
        self._nominal_AudioDeviceInput = None  # type: unique symbol

class AudioDeviceOutput:
    def __init__(self):
        self._nominal_AudioDeviceOutput = None  # type: unique symbol

class AudioDistortion:
    def __init__(self):
        self._nominal_AudioDistortion = None  # type: unique symbol

class AudioEcho:
    def __init__(self):
        self._nominal_AudioEcho = None  # type: unique symbol

class AudioEmitter:
    def __init__(self):
        self._nominal_AudioEmitter = None  # type: unique symbol

class AudioEqualizer:
    def __init__(self):
        self._nominal_AudioEqualizer = None  # type: unique symbol

class AudioFader:
    def __init__(self):
        self._nominal_AudioFader = None  # type: unique symbol

class AudioFilter:
    def __init__(self):
        self._nominal_AudioFilter = None  # type: unique symbol

class AudioFlanger:
    def __init__(self):
        self._nominal_AudioFlanger = None  # type: unique symbol

class AudioFocusService:
    def __init__(self):
        self._nominal_AudioFocusService = None  # type: unique symbol

class AudioLimiter:
    def __init__(self):
        self._nominal_AudioLimiter = None  # type: unique symbol

class AudioListener:
    def __init__(self):
        self._nominal_AudioListener = None  # type: unique symbol

class AudioPitchShifter:
    def __init__(self):
        self._nominal_AudioPitchShifter = None  # type: unique symbol

class AudioPlayer:
    def __init__(self):
        self._nominal_AudioPlayer = None  # type: unique symbol

class AudioRecorder:
    def __init__(self):
        self._nominal_AudioRecorder = None  # type: unique symbol

class AudioReverb:
    def __init__(self):
        self._nominal_AudioReverb = None  # type: unique symbol

class AudioSearchParams:
    def __init__(self):
        self._nominal_AudioSearchParams = None  # type: unique symbol

class AudioTextToSpeech:
    def __init__(self):
        self._nominal_AudioTextToSpeech = None  # type: unique symbol

class AuroraScriptObject:
    def __init__(self):
        self._nominal_AuroraScriptObject = None  # type: unique symbol

class AuroraScriptService:
    def __init__(self):
        self._nominal_AuroraScriptService = None  # type: unique symbol

class AuroraService:
    def __init__(self):
        self._nominal_AuroraService = None  # type: unique symbol

class AvatarAccessoryRules:
    def __init__(self):
        self._nominal_AvatarAccessoryRules = None  # type: unique symbol

class AvatarAnimationRules:
    def __init__(self):
        self._nominal_AvatarAnimationRules = None  # type: unique symbol

class AvatarBodyRules:
    def __init__(self):
        self._nominal_AvatarBodyRules = None  # type: unique symbol

class AvatarChatService:
    def __init__(self):
        self._nominal_AvatarChatService = None  # type: unique symbol

class AvatarClothingRules:
    def __init__(self):
        self._nominal_AvatarClothingRules = None  # type: unique symbol

class AvatarCollisionRules:
    def __init__(self):
        self._nominal_AvatarCollisionRules = None  # type: unique symbol

class AvatarCreationService:
    def __init__(self):
        self._nominal_AvatarCreationService = None  # type: unique symbol

class AvatarEditorService:
    def __init__(self):
        self._nominal_AvatarEditorService = None  # type: unique symbol

class AvatarImportService:
    def __init__(self):
        self._nominal_AvatarImportService = None  # type: unique symbol

class AvatarPreloader:
    def __init__(self):
        self._nominal_AvatarPreloader = None  # type: unique symbol

class AvatarRules:
    def __init__(self):
        self._nominal_AvatarRules = None  # type: unique symbol

class AvatarSettings:
    def __init__(self):
        self._nominal_AvatarSettings = None  # type: unique symbol

class Backpack:
    def __init__(self):
        self._nominal_Backpack = None  # type: unique symbol

class BadgeService:
    def __init__(self):
        self._nominal_BadgeService = None  # type: unique symbol

class BaseImportData:
    def __init__(self):
        self._nominal_BaseImportData = None  # type: unique symbol

class AnimationImportData:
    def __init__(self):
        self._nominal_AnimationImportData = None  # type: unique symbol

class FacsImportData:
    def __init__(self):
        self._nominal_FacsImportData = None  # type: unique symbol

class GroupImportData:
    def __init__(self):
        self._nominal_GroupImportData = None  # type: unique symbol

class JointImportData:
    def __init__(self):
        self._nominal_JointImportData = None  # type: unique symbol

class MaterialImportData:
    def __init__(self):
        self._nominal_MaterialImportData = None  # type: unique symbol

class MeshImportData:
    def __init__(self):
        self._nominal_MeshImportData = None  # type: unique symbol

class RootImportData:
    def __init__(self):
        self._nominal_RootImportData = None  # type: unique symbol

class BasePlayerGui:
    def __init__(self):
        self._nominal_BasePlayerGui = None  # type: unique symbol

class PlayerGui:
    def __init__(self):
        self._nominal_PlayerGui = None  # type: unique symbol

class StarterGui:
    def __init__(self):
        self._nominal_StarterGui = None  # type: unique symbol
        self.ProcessUserInput = None  # type: bool

class BaseRemoteEvent:
    def __init__(self):
        self._nominal_BaseRemoteEvent = None  # type: unique symbol

class RemoteEvent:
    def __init__(self):
        self._nominal_RemoteEvent = None  # type: unique symbol

class UnreliableRemoteEvent:
    def __init__(self):
        self._nominal_UnreliableRemoteEvent = None  # type: unique symbol

class BaseWrap:
    def __init__(self):
        self._nominal_BaseWrap = None  # type: unique symbol

class WrapDeformer:
    def __init__(self):
        self._nominal_WrapDeformer = None  # type: unique symbol

class WrapLayer:
    def __init__(self):
        self._nominal_WrapLayer = None  # type: unique symbol

class WrapTarget:
    def __init__(self):
        self._nominal_WrapTarget = None  # type: unique symbol

class Beam:
    def __init__(self):
        self._nominal_Beam = None  # type: unique symbol

class BindableEvent:
    def __init__(self):
        self._nominal_BindableEvent = None  # type: unique symbol

class BindableFunction:
    def __init__(self):
        self._nominal_BindableFunction = None  # type: unique symbol

class BodyMover:
    def __init__(self):
        self._nominal_BodyMover = None  # type: unique symbol

class BodyAngularVelocity:
    def __init__(self):
        self._nominal_BodyAngularVelocity = None  # type: unique symbol

class BodyForce:
    def __init__(self):
        self._nominal_BodyForce = None  # type: unique symbol

class BodyGyro:
    def __init__(self):
        self._nominal_BodyGyro = None  # type: unique symbol

class BodyPosition:
    def __init__(self):
        self._nominal_BodyPosition = None  # type: unique symbol

class BodyThrust:
    def __init__(self):
        self._nominal_BodyThrust = None  # type: unique symbol

class BodyVelocity:
    def __init__(self):
        self._nominal_BodyVelocity = None  # type: unique symbol

class RocketPropulsion:
    def __init__(self):
        self._nominal_RocketPropulsion = None  # type: unique symbol

class BodyPartDescription:
    def __init__(self):
        self._nominal_BodyPartDescription = None  # type: unique symbol

class Breakpoint:
    def __init__(self):
        self._nominal_Breakpoint = None  # type: unique symbol

class BugReporterService:
    def __init__(self):
        self._nominal_BugReporterService = None  # type: unique symbol

class BulkImportService:
    def __init__(self):
        self._nominal_BulkImportService = None  # type: unique symbol

class CalloutService:
    def __init__(self):
        self._nominal_CalloutService = None  # type: unique symbol

class CaptureService:
    def __init__(self):
        self._nominal_CaptureService = None  # type: unique symbol

class CharacterAppearance:
    def __init__(self):
        self._nominal_CharacterAppearance = None  # type: unique symbol

class BodyColors:
    def __init__(self):
        self._nominal_BodyColors = None  # type: unique symbol

class CharacterMesh:
    def __init__(self):
        self._nominal_CharacterMesh = None  # type: unique symbol

class Clothing:
    def __init__(self):
        self._nominal_Clothing = None  # type: unique symbol

class Pants:
    def __init__(self):
        self._nominal_Pants = None  # type: unique symbol

class Shirt:
    def __init__(self):
        self._nominal_Shirt = None  # type: unique symbol

class ShirtGraphic:
    def __init__(self):
        self._nominal_ShirtGraphic = None  # type: unique symbol

class Chat:
    def __init__(self):
        self._nominal_Chat = None  # type: unique symbol

class ChatbotUIService:
    def __init__(self):
        self._nominal_ChatbotUIService = None  # type: unique symbol

class ClickDetector:
    def __init__(self):
        self._nominal_ClickDetector = None  # type: unique symbol

class DragDetector:
    def __init__(self):
        self._nominal_DragDetector = None  # type: unique symbol

class CloudCRUDService:
    def __init__(self):
        self._nominal_CloudCRUDService = None  # type: unique symbol

class Clouds:
    def __init__(self):
        self._nominal_Clouds = None  # type: unique symbol

class Collaborator:
    def __init__(self):
        self._nominal_Collaborator = None  # type: unique symbol

class CollaboratorsService:
    def __init__(self):
        self._nominal_CollaboratorsService = None  # type: unique symbol

class CollectionService:
    def __init__(self):
        self._nominal_CollectionService = None  # type: unique symbol

class CommandInstance:
    def __init__(self):
        self._nominal_CommandInstance = None  # type: unique symbol

class CommandService:
    def __init__(self):
        self._nominal_CommandService = None  # type: unique symbol

class CommerceService:
    def __init__(self):
        self._nominal_CommerceService = None  # type: unique symbol

class ConfigService:
    def __init__(self):
        self._nominal_ConfigService = None  # type: unique symbol

class Configuration:
    def __init__(self):
        self._nominal_Configuration = None  # type: unique symbol

class ConfigureServerService:
    def __init__(self):
        self._nominal_ConfigureServerService = None  # type: unique symbol

class ConnectivityService:
    def __init__(self):
        self._nominal_ConnectivityService = None  # type: unique symbol

class Constraint:
    def __init__(self):
        self._nominal_Constraint = None  # type: unique symbol

class AlignOrientation:
    def __init__(self):
        self._nominal_AlignOrientation = None  # type: unique symbol

class AlignPosition:
    def __init__(self):
        self._nominal_AlignPosition = None  # type: unique symbol

class AngularVelocity:
    def __init__(self):
        self._nominal_AngularVelocity = None  # type: unique symbol

class AnimationConstraint:
    def __init__(self):
        self._nominal_AnimationConstraint = None  # type: unique symbol

class BallSocketConstraint:
    def __init__(self):
        self._nominal_BallSocketConstraint = None  # type: unique symbol

class HingeConstraint:
    def __init__(self):
        self._nominal_HingeConstraint = None  # type: unique symbol

class LineForce:
    def __init__(self):
        self._nominal_LineForce = None  # type: unique symbol

class LinearVelocity:
    def __init__(self):
        self._nominal_LinearVelocity = None  # type: unique symbol

class PlaneConstraint:
    def __init__(self):
        self._nominal_PlaneConstraint = None  # type: unique symbol

class Plane:
    def __init__(self):
        self._nominal_Plane = None  # type: unique symbol

class RigidConstraint:
    def __init__(self):
        self._nominal_RigidConstraint = None  # type: unique symbol

class RodConstraint:
    def __init__(self):
        self._nominal_RodConstraint = None  # type: unique symbol

class RopeConstraint:
    def __init__(self):
        self._nominal_RopeConstraint = None  # type: unique symbol

class SlidingBallConstraint:
    def __init__(self):
        self._nominal_SlidingBallConstraint = None  # type: unique symbol

class CylindricalConstraint:
    def __init__(self):
        self._nominal_CylindricalConstraint = None  # type: unique symbol

class PrismaticConstraint:
    def __init__(self):
        self._nominal_PrismaticConstraint = None  # type: unique symbol

class SpringConstraint:
    def __init__(self):
        self._nominal_SpringConstraint = None  # type: unique symbol

class Torque:
    def __init__(self):
        self._nominal_Torque = None  # type: unique symbol

class TorsionSpringConstraint:
    def __init__(self):
        self._nominal_TorsionSpringConstraint = None  # type: unique symbol

class UniversalConstraint:
    def __init__(self):
        self._nominal_UniversalConstraint = None  # type: unique symbol

class VectorForce:
    def __init__(self):
        self._nominal_VectorForce = None  # type: unique symbol

class ContentProvider:
    def __init__(self):
        self._nominal_ContentProvider = None  # type: unique symbol

class ContextActionService:
    def __init__(self):
        self._nominal_ContextActionService = None  # type: unique symbol

class Controller:
    def __init__(self):
        self._nominal_Controller = None  # type: unique symbol

class HumanoidController:
    def __init__(self):
        self._nominal_HumanoidController = None  # type: unique symbol

class SkateboardController:
    def __init__(self):
        self._nominal_SkateboardController = None  # type: unique symbol

class VehicleController:
    def __init__(self):
        self._nominal_VehicleController = None  # type: unique symbol

class ControllerBase:
    def __init__(self):
        self._nominal_ControllerBase = None  # type: unique symbol

class AirController:
    def __init__(self):
        self._nominal_AirController = None  # type: unique symbol

class ClimbController:
    def __init__(self):
        self._nominal_ClimbController = None  # type: unique symbol

class GroundController:
    def __init__(self):
        self._nominal_GroundController = None  # type: unique symbol

class SwimController:
    def __init__(self):
        self._nominal_SwimController = None  # type: unique symbol

class ControllerManager:
    def __init__(self):
        self._nominal_ControllerManager = None  # type: unique symbol

class ControllerService:
    def __init__(self):
        self._nominal_ControllerService = None  # type: unique symbol

class ConversationalAIAcceptanceService:
    def __init__(self):
        self._nominal_ConversationalAIAcceptanceService = None  # type: unique symbol

class CoreScriptDebuggingManagerHelper:
    def __init__(self):
        self._nominal_CoreScriptDebuggingManagerHelper = None  # type: unique symbol

class CreationDBService:
    def __init__(self):
        self._nominal_CreationDBService = None  # type: unique symbol

class CreatorStoreService:
    def __init__(self):
        self._nominal_CreatorStoreService = None  # type: unique symbol

class CrossDMScriptChangeListener:
    def __init__(self):
        self._nominal_CrossDMScriptChangeListener = None  # type: unique symbol

class CustomLog:
    def __init__(self):
        self._nominal_CustomLog = None  # type: unique symbol

class DataModelMesh:
    def __init__(self):
        self._nominal_DataModelMesh = None  # type: unique symbol

class BevelMesh:
    def __init__(self):
        self._nominal_BevelMesh = None  # type: unique symbol

class BlockMesh:
    def __init__(self):
        self._nominal_BlockMesh = None  # type: unique symbol

class CylinderMesh:
    def __init__(self):
        self._nominal_CylinderMesh = None  # type: unique symbol

class FileMesh:
    def __init__(self):
        self._nominal_FileMesh = None  # type: unique symbol

class SpecialMesh:
    def __init__(self):
        self._nominal_SpecialMesh = None  # type: unique symbol

class DataModelPatchService:
    def __init__(self):
        self._nominal_DataModelPatchService = None  # type: unique symbol

class DataStoreGetOptions:
    def __init__(self):
        self._nominal_DataStoreGetOptions = None  # type: unique symbol

class DataStoreIncrementOptions:
    def __init__(self):
        self._nominal_DataStoreIncrementOptions = None  # type: unique symbol

class DataStoreInfo:
    def __init__(self):
        self._nominal_DataStoreInfo = None  # type: unique symbol

class DataStoreKey:
    def __init__(self):
        self._nominal_DataStoreKey = None  # type: unique symbol

class DataStoreKeyInfo:
    def __init__(self):
        self._nominal_DataStoreKeyInfo = None  # type: unique symbol

class DataStoreObjectVersionInfo:
    def __init__(self):
        self._nominal_DataStoreObjectVersionInfo = None  # type: unique symbol

class DataStoreOptions:
    def __init__(self):
        self._nominal_DataStoreOptions = None  # type: unique symbol

class DataStoreService:
    def __init__(self):
        self._nominal_DataStoreService = None  # type: unique symbol

class DataStoreSetOptions:
    def __init__(self):
        self._nominal_DataStoreSetOptions = None  # type: unique symbol

class Debris:
    def __init__(self):
        self._nominal_Debris = None  # type: unique symbol

class DebuggablePluginWatcher:
    def __init__(self):
        self._nominal_DebuggablePluginWatcher = None  # type: unique symbol

class DebuggerConnection:
    def __init__(self):
        self._nominal_DebuggerConnection = None  # type: unique symbol

class LocalDebuggerConnection:
    def __init__(self):
        self._nominal_LocalDebuggerConnection = None  # type: unique symbol

class DebuggerConnectionManager:
    def __init__(self):
        self._nominal_DebuggerConnectionManager = None  # type: unique symbol

class DebuggerLuaResponse:
    def __init__(self):
        self._nominal_DebuggerLuaResponse = None  # type: unique symbol

class DebuggerUIService:
    def __init__(self):
        self._nominal_DebuggerUIService = None  # type: unique symbol

class DebuggerVariable:
    def __init__(self):
        self._nominal_DebuggerVariable = None  # type: unique symbol

class DeviceIdService:
    def __init__(self):
        self._nominal_DeviceIdService = None  # type: unique symbol

class Dialog:
    def __init__(self):
        self._nominal_Dialog = None  # type: unique symbol

class DialogChoice:
    def __init__(self):
        self._nominal_DialogChoice = None  # type: unique symbol

class Dragger:
    def __init__(self):
        self._nominal_Dragger = None  # type: unique symbol

class DraggerService:
    def __init__(self):
        self._nominal_DraggerService = None  # type: unique symbol

class EditableService:
    def __init__(self):
        self._nominal_EditableService = None  # type: unique symbol

class EulerRotationCurve:
    def __init__(self):
        self._nominal_EulerRotationCurve = None  # type: unique symbol

class EventIngestService:
    def __init__(self):
        self._nominal_EventIngestService = None  # type: unique symbol

class ExampleService:
    def __init__(self):
        self._nominal_ExampleService = None  # type: unique symbol

class ExperienceAuthService:
    def __init__(self):
        self._nominal_ExperienceAuthService = None  # type: unique symbol

class ExperienceInviteOptions:
    def __init__(self):
        self._nominal_ExperienceInviteOptions = None  # type: unique symbol

class ExperienceNotificationService:
    def __init__(self):
        self._nominal_ExperienceNotificationService = None  # type: unique symbol

class ExperienceService:
    def __init__(self):
        self._nominal_ExperienceService = None  # type: unique symbol

class ExperienceStateCaptureService:
    def __init__(self):
        self._nominal_ExperienceStateCaptureService = None  # type: unique symbol

class ExplorerFilter:
    def __init__(self):
        self._nominal_ExplorerFilter = None  # type: unique symbol

class ExplorerFilterAutocompleter:
    def __init__(self):
        self._nominal_ExplorerFilterAutocompleter = None  # type: unique symbol

class ExplorerServiceVisibilityService:
    def __init__(self):
        self._nominal_ExplorerServiceVisibilityService = None  # type: unique symbol

class Explosion:
    def __init__(self):
        self._nominal_Explosion = None  # type: unique symbol

class FaceAnimatorService:
    def __init__(self):
        self._nominal_FaceAnimatorService = None  # type: unique symbol

class FaceControls:
    def __init__(self):
        self._nominal_FaceControls = None  # type: unique symbol
        self.ChinRaiser = None  # type: float
        self.ChinRaiserUpperLip = None  # type: float
        self.Corrugator = None  # type: float
        self.EyesLookDown = None  # type: float
        self.EyesLookLeft = None  # type: float
        self.EyesLookRight = None  # type: float
        self.EyesLookUp = None  # type: float
        self.FlatPucker = None  # type: float
        self.Funneler = None  # type: float
        self.JawDrop = None  # type: float
        self.JawLeft = None  # type: float
        self.JawRight = None  # type: float
        self.LeftBrowLowerer = None  # type: float
        self.LeftCheekPuff = None  # type: float
        self.LeftCheekRaiser = None  # type: float
        self.LeftDimpler = None  # type: float
        self.LeftEyeClosed = None  # type: float
        self.LeftEyeUpperLidRaiser = None  # type: float
        self.LeftInnerBrowRaiser = None  # type: float
        self.LeftLipCornerDown = None  # type: float
        self.LeftLipCornerPuller = None  # type: float
        self.LeftLipStretcher = None  # type: float
        self.LeftLowerLipDepressor = None  # type: float
        self.LeftNoseWrinkler = None  # type: float
        self.LeftOuterBrowRaiser = None  # type: float
        self.LeftUpperLipRaiser = None  # type: float
        self.LipPresser = None  # type: float
        self.LipsTogether = None  # type: float
        self.LowerLipSuck = None  # type: float
        self.MouthLeft = None  # type: float
        self.MouthRight = None  # type: float
        self.Pucker = None  # type: float
        self.RightBrowLowerer = None  # type: float
        self.RightCheekPuff = None  # type: float
        self.RightCheekRaiser = None  # type: float
        self.RightDimpler = None  # type: float
        self.RightEyeClosed = None  # type: float
        self.RightEyeUpperLidRaiser = None  # type: float
        self.RightInnerBrowRaiser = None  # type: float
        self.RightLipCornerDown = None  # type: float
        self.RightLipCornerPuller = None  # type: float
        self.RightLipStretcher = None  # type: float
        self.RightLowerLipDepressor = None  # type: float
        self.RightNoseWrinkler = None  # type: float
        self.RightOuterBrowRaiser = None  # type: float
        self.RightUpperLipRaiser = None  # type: float
        self.TongueDown = None  # type: float
        self.TongueOut = None  # type: float
        self.TongueUp = None  # type: float
        self.UpperLipSuck = None  # type: float

class FaceInstance:
    def __init__(self):
        self._nominal_FaceInstance = None  # type: unique symbol

class Decal:
    def __init__(self):
        self._nominal_Decal = None  # type: unique symbol

class Texture:
    def __init__(self):
        self._nominal_Texture = None  # type: unique symbol

class FacialAgeEstimationService:
    def __init__(self):
        self._nominal_FacialAgeEstimationService = None  # type: unique symbol

class FacialAnimationRecordingService:
    def __init__(self):
        self._nominal_FacialAnimationRecordingService = None  # type: unique symbol

class FacialAnimationStreamingServiceStats:
    def __init__(self):
        self._nominal_FacialAnimationStreamingServiceStats = None  # type: unique symbol

class FacialAnimationStreamingServiceV2:
    def __init__(self):
        self._nominal_FacialAnimationStreamingServiceV2 = None  # type: unique symbol

class FacialAnimationStreamingSubsessionStats:
    def __init__(self):
        self._nominal_FacialAnimationStreamingSubsessionStats = None  # type: unique symbol

class Feature:
    def __init__(self):
        self._nominal_Feature = None  # type: unique symbol

class Hole:
    def __init__(self):
        self._nominal_Hole = None  # type: unique symbol

class MotorFeature:
    def __init__(self):
        self._nominal_MotorFeature = None  # type: unique symbol

class FeatureRestrictionManager:
    def __init__(self):
        self._nominal_FeatureRestrictionManager = None  # type: unique symbol

class FeedService:
    def __init__(self):
        self._nominal_FeedService = None  # type: unique symbol

class Fire:
    def __init__(self):
        self._nominal_Fire = None  # type: unique symbol

class FloatCurve:
    def __init__(self):
        self._nominal_FloatCurve = None  # type: unique symbol

class Folder:
    def __init__(self):
        self._nominal_Folder = None  # type: unique symbol

class ForceField:
    def __init__(self):
        self._nominal_ForceField = None  # type: unique symbol

class GamePassService:
    def __init__(self):
        self._nominal_GamePassService = None  # type: unique symbol

class GamepadService:
    def __init__(self):
        self._nominal_GamepadService = None  # type: unique symbol

class GenerationService:
    def __init__(self):
        self._nominal_GenerationService = None  # type: unique symbol

class GenericChallengeService:
    def __init__(self):
        self._nominal_GenericChallengeService = None  # type: unique symbol

class GeometryService:
    def __init__(self):
        self._nominal_GeometryService = None  # type: unique symbol

class GetTextBoundsParams:
    def __init__(self):
        self._nominal_GetTextBoundsParams = None  # type: unique symbol

class GlobalDataStore:
    def __init__(self):
        self._nominal_GlobalDataStore = None  # type: unique symbol

class DataStore:
    def __init__(self):
        self._nominal_DataStore = None  # type: unique symbol

class OrderedDataStore:
    def __init__(self):
        self._nominal_OrderedDataStore = None  # type: unique symbol

class GroupService:
    def __init__(self):
        self._nominal_GroupService = None  # type: unique symbol

class GuiBase:
    def __init__(self):
        self._nominal_GuiBase = None  # type: unique symbol

class GuiBase2d:
    def __init__(self):
        self._nominal_GuiBase2d = None  # type: unique symbol

class GuiObject:
    def __init__(self):
        self._nominal_GuiObject = None  # type: unique symbol

class CanvasGroup:
    def __init__(self):
        self._nominal_CanvasGroup = None  # type: unique symbol

class Frame:
    def __init__(self):
        self._nominal_Frame = None  # type: unique symbol

class GuiButton:
    def __init__(self):
        self._nominal_GuiButton = None  # type: unique symbol

class ImageButton:
    def __init__(self):
        self._nominal_ImageButton = None  # type: unique symbol

class TextButton:
    def __init__(self):
        self._nominal_TextButton = None  # type: unique symbol

class GuiLabel:
    def __init__(self):
        self._nominal_GuiLabel = None  # type: unique symbol

class ImageLabel:
    def __init__(self):
        self._nominal_ImageLabel = None  # type: unique symbol

class TextLabel:
    def __init__(self):
        self._nominal_TextLabel = None  # type: unique symbol

class RelativeGui:
    def __init__(self):
        self._nominal_RelativeGui = None  # type: unique symbol

class ScrollingFrame:
    def __init__(self):
        self._nominal_ScrollingFrame = None  # type: unique symbol

class TextBox:
    def __init__(self):
        self._nominal_TextBox = None  # type: unique symbol

class VideoDisplay:
    def __init__(self):
        self._nominal_VideoDisplay = None  # type: unique symbol

class VideoFrame:
    def __init__(self):
        self._nominal_VideoFrame = None  # type: unique symbol

class ViewportFrame:
    def __init__(self):
        self._nominal_ViewportFrame = None  # type: unique symbol

class LayerCollector:
    def __init__(self):
        self._nominal_LayerCollector = None  # type: unique symbol

class BillboardGui:
    def __init__(self):
        self._nominal_BillboardGui = None  # type: unique symbol

class ScreenGui:
    def __init__(self):
        self._nominal_ScreenGui = None  # type: unique symbol

class SurfaceGuiBase:
    def __init__(self):
        self._nominal_SurfaceGuiBase = None  # type: unique symbol

class AdGui:
    def __init__(self):
        self._nominal_AdGui = None  # type: unique symbol

class SurfaceGui:
    def __init__(self):
        self._nominal_SurfaceGui = None  # type: unique symbol

class GuiBase3d:
    def __init__(self):
        self._nominal_GuiBase3d = None  # type: unique symbol

class FloorWire:
    def __init__(self):
        self._nominal_FloorWire = None  # type: unique symbol

class InstanceAdornment:
    def __init__(self):
        self._nominal_InstanceAdornment = None  # type: unique symbol

class SelectionBox:
    def __init__(self):
        self._nominal_SelectionBox = None  # type: unique symbol

class PVAdornment:
    def __init__(self):
        self._nominal_PVAdornment = None  # type: unique symbol

class HandleAdornment:
    def __init__(self):
        self._nominal_HandleAdornment = None  # type: unique symbol

class BoxHandleAdornment:
    def __init__(self):
        self._nominal_BoxHandleAdornment = None  # type: unique symbol

class ConeHandleAdornment:
    def __init__(self):
        self._nominal_ConeHandleAdornment = None  # type: unique symbol

class CylinderHandleAdornment:
    def __init__(self):
        self._nominal_CylinderHandleAdornment = None  # type: unique symbol

class ImageHandleAdornment:
    def __init__(self):
        self._nominal_ImageHandleAdornment = None  # type: unique symbol

class LineHandleAdornment:
    def __init__(self):
        self._nominal_LineHandleAdornment = None  # type: unique symbol

class SphereHandleAdornment:
    def __init__(self):
        self._nominal_SphereHandleAdornment = None  # type: unique symbol

class WireframeHandleAdornment:
    def __init__(self):
        self._nominal_WireframeHandleAdornment = None  # type: unique symbol

class ParabolaAdornment:
    def __init__(self):
        self._nominal_ParabolaAdornment = None  # type: unique symbol

class SelectionSphere:
    def __init__(self):
        self._nominal_SelectionSphere = None  # type: unique symbol

class PartAdornment:
    def __init__(self):
        self._nominal_PartAdornment = None  # type: unique symbol

class HandlesBase:
    def __init__(self):
        self._nominal_HandlesBase = None  # type: unique symbol

class ArcHandles:
    def __init__(self):
        self._nominal_ArcHandles = None  # type: unique symbol

class Handles:
    def __init__(self):
        self._nominal_Handles = None  # type: unique symbol

class SurfaceSelection:
    def __init__(self):
        self._nominal_SurfaceSelection = None  # type: unique symbol

class SelectionLasso:
    def __init__(self):
        self._nominal_SelectionLasso = None  # type: unique symbol

class SelectionPartLasso:
    def __init__(self):
        self._nominal_SelectionPartLasso = None  # type: unique symbol

class SelectionPointLasso:
    def __init__(self):
        self._nominal_SelectionPointLasso = None  # type: unique symbol

class Path2D:
    def __init__(self):
        self._nominal_Path2D = None  # type: unique symbol

class GuiService:
    def __init__(self):
        self._nominal_GuiService = None  # type: unique symbol

class HandRigDescription:
    def __init__(self):
        self._nominal_HandRigDescription = None  # type: unique symbol

class HapticEffect:
    def __init__(self):
        self._nominal_HapticEffect = None  # type: unique symbol

class HapticService:
    def __init__(self):
        self._nominal_HapticService = None  # type: unique symbol

class HeapProfilerService:
    def __init__(self):
        self._nominal_HeapProfilerService = None  # type: unique symbol
        self.OnNewData = None  # type: RBXScriptSignal<(player: Player, jsonString: buffer, id: float, compressedLength: float, uncompressedLength: float) => void>

class HeatmapService:
    def __init__(self):
        self._nominal_HeatmapService = None  # type: unique symbol

class HeightmapImporterService:
    def __init__(self):
        self._nominal_HeightmapImporterService = None  # type: unique symbol

class HiddenSurfaceRemovalAsset:
    def __init__(self):
        self._nominal_HiddenSurfaceRemovalAsset = None  # type: unique symbol

class Highlight:
    def __init__(self):
        self._nominal_Highlight = None  # type: unique symbol

class HttpService:
    def __init__(self):
        self._nominal_HttpService = None  # type: unique symbol

class Humanoid:
    def __init__(self):
        self._nominal_Humanoid = None  # type: unique symbol

class HumanoidDescription:
    def __init__(self):
        self._nominal_HumanoidDescription = None  # type: unique symbol

class HumanoidRigDescription:
    def __init__(self):
        self._nominal_HumanoidRigDescription = None  # type: unique symbol

class IKControl:
    def __init__(self):
        self._nominal_IKControl = None  # type: unique symbol

class ILegacyStudioBridge:
    def __init__(self):
        self._nominal_ILegacyStudioBridge = None  # type: unique symbol

class LegacyStudioBridge:
    def __init__(self):
        self._nominal_LegacyStudioBridge = None  # type: unique symbol

class IXPService:
    def __init__(self):
        self._nominal_IXPService = None  # type: unique symbol

class ImportSession:
    def __init__(self):
        self._nominal_ImportSession = None  # type: unique symbol

class AssetImportSession:
    def __init__(self):
        self._nominal_AssetImportSession = None  # type: unique symbol

class IncrementalPatchBuilder:
    def __init__(self):
        self._nominal_IncrementalPatchBuilder = None  # type: unique symbol

class InputAction:
    def __init__(self):
        self._nominal_InputAction = None  # type: unique symbol

class InputBinding:
    def __init__(self):
        self._nominal_InputBinding = None  # type: unique symbol

class InputContext:
    def __init__(self):
        self._nominal_InputContext = None  # type: unique symbol

class InputObject:
    def __init__(self):
        self._nominal_InputObject = None  # type: unique symbol

class InsertService:
    def __init__(self):
        self._nominal_InsertService = None  # type: unique symbol

class InternalSyncItem:
    def __init__(self):
        self._nominal_InternalSyncItem = None  # type: unique symbol

class InternalSyncService:
    def __init__(self):
        self._nominal_InternalSyncService = None  # type: unique symbol

class JointInstance:
    def __init__(self):
        self._nominal_JointInstance = None  # type: unique symbol

class DynamicRotate:
    def __init__(self):
        self._nominal_DynamicRotate = None  # type: unique symbol

class RotateP:
    def __init__(self):
        self._nominal_RotateP = None  # type: unique symbol

class RotateV:
    def __init__(self):
        self._nominal_RotateV = None  # type: unique symbol

class Glue:
    def __init__(self):
        self._nominal_Glue = None  # type: unique symbol

class ManualSurfaceJointInstance:
    def __init__(self):
        self._nominal_ManualSurfaceJointInstance = None  # type: unique symbol

class ManualGlue:
    def __init__(self):
        self._nominal_ManualGlue = None  # type: unique symbol

class ManualWeld:
    def __init__(self):
        self._nominal_ManualWeld = None  # type: unique symbol

class Motor:
    def __init__(self):
        self._nominal_Motor = None  # type: unique symbol

class Motor6D:
    def __init__(self):
        self._nominal_Motor6D = None  # type: unique symbol

class Rotate:
    def __init__(self):
        self._nominal_Rotate = None  # type: unique symbol

class Snap:
    def __init__(self):
        self._nominal_Snap = None  # type: unique symbol

class VelocityMotor:
    def __init__(self):
        self._nominal_VelocityMotor = None  # type: unique symbol

class Weld:
    def __init__(self):
        self._nominal_Weld = None  # type: unique symbol

class JointsService:
    def __init__(self):
        self._nominal_JointsService = None  # type: unique symbol

class Keyframe:
    def __init__(self):
        self._nominal_Keyframe = None  # type: unique symbol

class KeyframeMarker:
    def __init__(self):
        self._nominal_KeyframeMarker = None  # type: unique symbol

class KeyframeSequenceProvider:
    def __init__(self):
        self._nominal_KeyframeSequenceProvider = None  # type: unique symbol

class LSPFileSyncService:
    def __init__(self):
        self._nominal_LSPFileSyncService = None  # type: unique symbol

class LanguageService:
    def __init__(self):
        self._nominal_LanguageService = None  # type: unique symbol

class Light:
    def __init__(self):
        self._nominal_Light = None  # type: unique symbol

class PointLight:
    def __init__(self):
        self._nominal_PointLight = None  # type: unique symbol

class SpotLight:
    def __init__(self):
        self._nominal_SpotLight = None  # type: unique symbol

class SurfaceLight:
    def __init__(self):
        self._nominal_SurfaceLight = None  # type: unique symbol

class Lighting:
    def __init__(self):
        self._nominal_Lighting = None  # type: unique symbol

class LinkingService:
    def __init__(self):
        self._nominal_LinkingService = None  # type: unique symbol

class LiveScriptingService:
    def __init__(self):
        self._nominal_LiveScriptingService = None  # type: unique symbol

class LiveSyncService:
    def __init__(self):
        self._nominal_LiveSyncService = None  # type: unique symbol

class LocalizationService:
    def __init__(self):
        self._nominal_LocalizationService = None  # type: unique symbol

class LocalizationTable:
    def __init__(self):
        self._nominal_LocalizationTable = None  # type: unique symbol

class CloudLocalizationTable:
    def __init__(self):
        self._nominal_CloudLocalizationTable = None  # type: unique symbol

class LodDataEntity:
    def __init__(self):
        self._nominal_LodDataEntity = None  # type: unique symbol

class LodDataService:
    def __init__(self):
        self._nominal_LodDataService = None  # type: unique symbol

class LogReporterService:
    def __init__(self):
        self._nominal_LogReporterService = None  # type: unique symbol

class LogService:
    def __init__(self):
        self._nominal_LogService = None  # type: unique symbol

class LuaSourceContainer:
    def __init__(self):
        self._nominal_LuaSourceContainer = None  # type: unique symbol

class AuroraScript:
    def __init__(self):
        self._nominal_AuroraScript = None  # type: unique symbol
        self.EnableCulling = None  # type: bool
        self.EnableLOD = None  # type: bool
        self.LODCriticality = None  # type: float
        self.Priority = None  # type: float
        self.Source = None  # type: ProtectedString

class BaseScript:
    def __init__(self):
        self._nominal_BaseScript = None  # type: unique symbol

class Script:
    def __init__(self):
        self._nominal_Script = None  # type: unique symbol

class LocalScript:
    def __init__(self):
        self._nominal_LocalScript = None  # type: unique symbol

class ModuleScript:
    def __init__(self):
        self._nominal_ModuleScript = None  # type: unique symbol

class LuauScriptAnalyzerService:
    def __init__(self):
        self._nominal_LuauScriptAnalyzerService = None  # type: unique symbol

class MLModelDeliveryService:
    def __init__(self):
        self._nominal_MLModelDeliveryService = None  # type: unique symbol

class MarkerCurve:
    def __init__(self):
        self._nominal_MarkerCurve = None  # type: unique symbol

class MarketplaceService:
    def __init__(self):
        self._nominal_MarketplaceService = None  # type: unique symbol

class MatchmakingService:
    def __init__(self):
        self._nominal_MatchmakingService = None  # type: unique symbol

class MaterialGenerationService:
    def __init__(self):
        self._nominal_MaterialGenerationService = None  # type: unique symbol

class MaterialGenerationSession:
    def __init__(self):
        self._nominal_MaterialGenerationSession = None  # type: unique symbol

class MaterialService:
    def __init__(self):
        self._nominal_MaterialService = None  # type: unique symbol

class MaterialVariant:
    def __init__(self):
        self._nominal_MaterialVariant = None  # type: unique symbol
        self.ColorMap = None  # type: ContentId
        self.ColorMapContent = None  # type: Content
        self.MetalnessMap = None  # type: ContentId
        self.MetalnessMapContent = None  # type: Content
        self.NormalMap = None  # type: ContentId
        self.NormalMapContent = None  # type: Content
        self.RoughnessMap = None  # type: ContentId
        self.RoughnessMapContent = None  # type: Content

class MemoryStoreHashMap:
    def __init__(self):
        self._nominal_MemoryStoreHashMap = None  # type: unique symbol

class MemoryStoreQueue:
    def __init__(self):
        self._nominal_MemoryStoreQueue = None  # type: unique symbol

class MemoryStoreService:
    def __init__(self):
        self._nominal_MemoryStoreService = None  # type: unique symbol

class MemoryStoreSortedMap:
    def __init__(self):
        self._nominal_MemoryStoreSortedMap = None  # type: unique symbol

class MessageBusConnection:
    def __init__(self):
        self._nominal_MessageBusConnection = None  # type: unique symbol

class MessageBusService:
    def __init__(self):
        self._nominal_MessageBusService = None  # type: unique symbol

class MessagingService:
    def __init__(self):
        self._nominal_MessagingService = None  # type: unique symbol

class MetaBreakpoint:
    def __init__(self):
        self._nominal_MetaBreakpoint = None  # type: unique symbol

class MetaBreakpointContext:
    def __init__(self):
        self._nominal_MetaBreakpointContext = None  # type: unique symbol

class MetaBreakpointManager:
    def __init__(self):
        self._nominal_MetaBreakpointManager = None  # type: unique symbol

class Mouse:
    def __init__(self):
        self._nominal_Mouse = None  # type: unique symbol

class PlayerMouse:
    def __init__(self):
        self._nominal_PlayerMouse = None  # type: unique symbol

class NetworkMarker:
    def __init__(self):
        self._nominal_NetworkMarker = None  # type: unique symbol

class NoCollisionConstraint:
    def __init__(self):
        self._nominal_NoCollisionConstraint = None  # type: unique symbol

class Noise:
    def __init__(self):
        self._nominal_Noise = None  # type: unique symbol

class OmniRecommendationsService:
    def __init__(self):
        self._nominal_OmniRecommendationsService = None  # type: unique symbol

class OpenCloudApiV1:
    def __init__(self):
        self._nominal_OpenCloudApiV1 = None  # type: unique symbol

class OpenCloudService:
    def __init__(self):
        self._nominal_OpenCloudService = None  # type: unique symbol

class OperationGraph:
    def __init__(self):
        self._nominal_OperationGraph = None  # type: unique symbol

class PVInstance:
    def __init__(self):
        self._nominal_PVInstance = None  # type: unique symbol

class BasePart:
    def __init__(self):
        self._nominal_BasePart = None  # type: unique symbol

class CornerWedgePart:
    def __init__(self):
        self._nominal_CornerWedgePart = None  # type: unique symbol

class FormFactorPart:
    def __init__(self):
        self._nominal_FormFactorPart = None  # type: unique symbol

class Part:
    def __init__(self):
        self._nominal_Part = None  # type: unique symbol

class Platform:
    def __init__(self):
        self._nominal_Platform = None  # type: unique symbol

class Seat:
    def __init__(self):
        self._nominal_Seat = None  # type: unique symbol

class SkateboardPlatform:
    def __init__(self):
        self._nominal_SkateboardPlatform = None  # type: unique symbol

class SpawnLocation:
    def __init__(self):
        self._nominal_SpawnLocation = None  # type: unique symbol

class WedgePart:
    def __init__(self):
        self._nominal_WedgePart = None  # type: unique symbol

class Terrain:
    def __init__(self):
        self._nominal_Terrain = None  # type: unique symbol

class TriangleMeshPart:
    def __init__(self):
        self._nominal_TriangleMeshPart = None  # type: unique symbol

class MeshPart:
    def __init__(self):
        self._nominal_MeshPart = None  # type: unique symbol

class PartOperation:
    def __init__(self):
        self._nominal_PartOperation = None  # type: unique symbol

class IntersectOperation:
    def __init__(self):
        self._nominal_IntersectOperation = None  # type: unique symbol

class NegateOperation:
    def __init__(self):
        self._nominal_NegateOperation = None  # type: unique symbol

class UnionOperation:
    def __init__(self):
        self._nominal_UnionOperation = None  # type: unique symbol

class TrussPart:
    def __init__(self):
        self._nominal_TrussPart = None  # type: unique symbol

class VehicleSeat:
    def __init__(self):
        self._nominal_VehicleSeat = None  # type: unique symbol

class Camera:
    def __init__(self):
        self._nominal_Camera = None  # type: unique symbol

class Model:
    def __init__(self):
        self._nominal_Model = None  # type: unique symbol
        self.LevelOfDetail = None  # type: Enum.ModelLevelOfDetail

class Actor:
    def __init__(self):
        self._nominal_Actor = None  # type: unique symbol

class BackpackItem:
    def __init__(self):
        self._nominal_BackpackItem = None  # type: unique symbol

class Tool:
    def __init__(self):
        self._nominal_Tool = None  # type: unique symbol

class WorldRoot:
    def __init__(self):
        self._nominal_WorldRoot = None  # type: unique symbol

class Workspace:
    def __init__(self):
        self._nominal_Workspace = None  # type: unique symbol
        self.BreakJoints = None  # type: never
        self.MakeJoints = None  # type: never

class WorldModel:
    def __init__(self):
        self._nominal_WorldModel = None  # type: unique symbol

class PackageLink:
    def __init__(self):
        self._nominal_PackageLink = None  # type: unique symbol

class PackageUIService:
    def __init__(self):
        self._nominal_PackageUIService = None  # type: unique symbol

class Pages:
    def __init__(self):
        self._nominal_Pages = None  # type: unique symbol

class AudioPages:
    def __init__(self):
        self._nominal_AudioPages = None  # type: unique symbol

class BanHistoryPages:
    def __init__(self):
        self._nominal_BanHistoryPages = None  # type: unique symbol

class CatalogPages:
    def __init__(self):
        self._nominal_CatalogPages = None  # type: unique symbol

class DataStoreKeyPages:
    def __init__(self):
        self._nominal_DataStoreKeyPages = None  # type: unique symbol

class DataStoreListingPages:
    def __init__(self):
        self._nominal_DataStoreListingPages = None  # type: unique symbol

class DataStorePages:
    def __init__(self):
        self._nominal_DataStorePages = None  # type: unique symbol

class DataStoreVersionPages:
    def __init__(self):
        self._nominal_DataStoreVersionPages = None  # type: unique symbol

class FeedPages:
    def __init__(self):
        self._nominal_FeedPages = None  # type: unique symbol

class FriendPages:
    def __init__(self):
        self._nominal_FriendPages = None  # type: unique symbol

class InventoryPages:
    def __init__(self):
        self._nominal_InventoryPages = None  # type: unique symbol

class EmotesPages:
    def __init__(self):
        self._nominal_EmotesPages = None  # type: unique symbol

class MemoryStoreHashMapPages:
    def __init__(self):
        self._nominal_MemoryStoreHashMapPages = None  # type: unique symbol

class OutfitPages:
    def __init__(self):
        self._nominal_OutfitPages = None  # type: unique symbol

class StandardPages:
    def __init__(self):
        self._nominal_StandardPages = None  # type: unique symbol

class ParticleEmitter:
    def __init__(self):
        self._nominal_ParticleEmitter = None  # type: unique symbol

class PatchBundlerFileWatch:
    def __init__(self):
        self._nominal_PatchBundlerFileWatch = None  # type: unique symbol

class PatchMapping:
    def __init__(self):
        self._nominal_PatchMapping = None  # type: unique symbol

class Path:
    def __init__(self):
        self._nominal_Path = None  # type: unique symbol

class PathfindingLink:
    def __init__(self):
        self._nominal_PathfindingLink = None  # type: unique symbol

class PathfindingModifier:
    def __init__(self):
        self._nominal_PathfindingModifier = None  # type: unique symbol

class PathfindingService:
    def __init__(self):
        self._nominal_PathfindingService = None  # type: unique symbol

class PausedState:
    def __init__(self):
        self._nominal_PausedState = None  # type: unique symbol

class PausedStateBreakpoint:
    def __init__(self):
        self._nominal_PausedStateBreakpoint = None  # type: unique symbol

class PausedStateException:
    def __init__(self):
        self._nominal_PausedStateException = None  # type: unique symbol

class PerformanceControlService:
    def __init__(self):
        self._nominal_PerformanceControlService = None  # type: unique symbol

class PhysicsService:
    def __init__(self):
        self._nominal_PhysicsService = None  # type: unique symbol

class PlaceAssetIdsService:
    def __init__(self):
        self._nominal_PlaceAssetIdsService = None  # type: unique symbol

class PlaceStatsService:
    def __init__(self):
        self._nominal_PlaceStatsService = None  # type: unique symbol

class PlacesService:
    def __init__(self):
        self._nominal_PlacesService = None  # type: unique symbol

class PlatformCloudStorageService:
    def __init__(self):
        self._nominal_PlatformCloudStorageService = None  # type: unique symbol

class PlatformFriendsService:
    def __init__(self):
        self._nominal_PlatformFriendsService = None  # type: unique symbol

class Player:
    def __init__(self):
        self._nominal_Player = None  # type: unique symbol
        self.Name = None  # type: str

class PlayerData:
    def __init__(self):
        self._nominal_PlayerData = None  # type: unique symbol

class PlayerDataRecord:
    def __init__(self):
        self._nominal_PlayerDataRecord = None  # type: unique symbol

class PlayerDataRecordConfig:
    def __init__(self):
        self._nominal_PlayerDataRecordConfig = None  # type: unique symbol

class PlayerDataService:
    def __init__(self):
        self._nominal_PlayerDataService = None  # type: unique symbol

class PlayerHydrationService:
    def __init__(self):
        self._nominal_PlayerHydrationService = None  # type: unique symbol

class PlayerScripts:
    def __init__(self):
        self._nominal_PlayerScripts = None  # type: unique symbol

class PlayerViewService:
    def __init__(self):
        self._nominal_PlayerViewService = None  # type: unique symbol

class Players:
    def __init__(self):
        self._nominal_Players = None  # type: unique symbol

class PluginCapabilities:
    def __init__(self):
        self._nominal_PluginCapabilities = None  # type: unique symbol

class PluginManagementService:
    def __init__(self):
        self._nominal_PluginManagementService = None  # type: unique symbol

class PluginManagerInterface:
    def __init__(self):
        self._nominal_PluginManagerInterface = None  # type: unique symbol

class PluginPolicyService:
    def __init__(self):
        self._nominal_PluginPolicyService = None  # type: unique symbol

class PolicyService:
    def __init__(self):
        self._nominal_PolicyService = None  # type: unique symbol

class PoseBase:
    def __init__(self):
        self._nominal_PoseBase = None  # type: unique symbol

class NumberPose:
    def __init__(self):
        self._nominal_NumberPose = None  # type: unique symbol

class Pose:
    def __init__(self):
        self._nominal_Pose = None  # type: unique symbol

class PostEffect:
    def __init__(self):
        self._nominal_PostEffect = None  # type: unique symbol

class BloomEffect:
    def __init__(self):
        self._nominal_BloomEffect = None  # type: unique symbol

class BlurEffect:
    def __init__(self):
        self._nominal_BlurEffect = None  # type: unique symbol

class ColorCorrectionEffect:
    def __init__(self):
        self._nominal_ColorCorrectionEffect = None  # type: unique symbol

class ColorGradingEffect:
    def __init__(self):
        self._nominal_ColorGradingEffect = None  # type: unique symbol

class DepthOfFieldEffect:
    def __init__(self):
        self._nominal_DepthOfFieldEffect = None  # type: unique symbol

class SunRaysEffect:
    def __init__(self):
        self._nominal_SunRaysEffect = None  # type: unique symbol

class ProcessInstancePhysicsService:
    def __init__(self):
        self._nominal_ProcessInstancePhysicsService = None  # type: unique symbol

class ProximityPrompt:
    def __init__(self):
        self._nominal_ProximityPrompt = None  # type: unique symbol

class ProximityPromptService:
    def __init__(self):
        self._nominal_ProximityPromptService = None  # type: unique symbol

class PublishService:
    def __init__(self):
        self._nominal_PublishService = None  # type: unique symbol

class RTAnimationTracker:
    def __init__(self):
        self._nominal_RTAnimationTracker = None  # type: unique symbol

class ReflectionService:
    def __init__(self):
        self._nominal_ReflectionService = None  # type: unique symbol

class RemoteCursorService:
    def __init__(self):
        self._nominal_RemoteCursorService = None  # type: unique symbol

class RemoteDebuggerServer:
    def __init__(self):
        self._nominal_RemoteDebuggerServer = None  # type: unique symbol

class RemoteFunction:
    def __init__(self):
        self._nominal_RemoteFunction = None  # type: unique symbol

class ReplicatedFirst:
    def __init__(self):
        self._nominal_ReplicatedFirst = None  # type: unique symbol

class ReplicatedStorage:
    def __init__(self):
        self._nominal_ReplicatedStorage = None  # type: unique symbol

class RibbonNotificationService:
    def __init__(self):
        self._nominal_RibbonNotificationService = None  # type: unique symbol

class RobloxSerializableInstance:
    def __init__(self):
        self._nominal_RobloxSerializableInstance = None  # type: unique symbol

class RobloxServerStorage:
    def __init__(self):
        self._nominal_RobloxServerStorage = None  # type: unique symbol

class RomarkRbxAnalyticsService:
    def __init__(self):
        self._nominal_RomarkRbxAnalyticsService = None  # type: unique symbol

class RomarkService:
    def __init__(self):
        self._nominal_RomarkService = None  # type: unique symbol

class RotationCurve:
    def __init__(self):
        self._nominal_RotationCurve = None  # type: unique symbol

class RtMessagingService:
    def __init__(self):
        self._nominal_RtMessagingService = None  # type: unique symbol

class RunService:
    def __init__(self):
        self._nominal_RunService = None  # type: unique symbol
        self.RunState = None  # type: Enum.RunState

class SafetyService:
    def __init__(self):
        self._nominal_SafetyService = None  # type: unique symbol

class ScreenshotHud:
    def __init__(self):
        self._nominal_ScreenshotHud = None  # type: unique symbol

class ScriptBuilder:
    def __init__(self):
        self._nominal_ScriptBuilder = None  # type: unique symbol

class SyncScriptBuilder:
    def __init__(self):
        self._nominal_SyncScriptBuilder = None  # type: unique symbol

class ScriptChangeService:
    def __init__(self):
        self._nominal_ScriptChangeService = None  # type: unique symbol

class ScriptCloneWatcher:
    def __init__(self):
        self._nominal_ScriptCloneWatcher = None  # type: unique symbol

class ScriptCloneWatcherHelper:
    def __init__(self):
        self._nominal_ScriptCloneWatcherHelper = None  # type: unique symbol

class ScriptCommitService:
    def __init__(self):
        self._nominal_ScriptCommitService = None  # type: unique symbol

class ScriptContext:
    def __init__(self):
        self._nominal_ScriptContext = None  # type: unique symbol

class ScriptProfilerService:
    def __init__(self):
        self._nominal_ScriptProfilerService = None  # type: unique symbol
        self.OnNewData = None  # type: RBXScriptSignal<(player: Player, jsonString: str) => void>

class ScriptRegistrationService:
    def __init__(self):
        self._nominal_ScriptRegistrationService = None  # type: unique symbol

class ScriptRuntime:
    def __init__(self):
        self._nominal_ScriptRuntime = None  # type: unique symbol

class SelectionHighlightManager:
    def __init__(self):
        self._nominal_SelectionHighlightManager = None  # type: unique symbol

class SensorBase:
    def __init__(self):
        self._nominal_SensorBase = None  # type: unique symbol

class AtmosphereSensor:
    def __init__(self):
        self._nominal_AtmosphereSensor = None  # type: unique symbol

class BuoyancySensor:
    def __init__(self):
        self._nominal_BuoyancySensor = None  # type: unique symbol

class ControllerSensor:
    def __init__(self):
        self._nominal_ControllerSensor = None  # type: unique symbol

class ControllerPartSensor:
    def __init__(self):
        self._nominal_ControllerPartSensor = None  # type: unique symbol

class FluidForceSensor:
    def __init__(self):
        self._nominal_FluidForceSensor = None  # type: unique symbol

class SerializationService:
    def __init__(self):
        self._nominal_SerializationService = None  # type: unique symbol

class ServerScriptService:
    def __init__(self):
        self._nominal_ServerScriptService = None  # type: unique symbol

class ServerStorage:
    def __init__(self):
        self._nominal_ServerStorage = None  # type: unique symbol

class ServiceProvider:
    def __init__(self):
        self._nominal_ServiceProvider = None  # type: unique symbol

class DataModel:
    def __init__(self):
        self._nominal_DataModel = None  # type: unique symbol

class GenericSettings:
    def __init__(self):
        self._nominal_GenericSettings = None  # type: unique symbol

class UserSettings:
    def __init__(self):
        self._nominal_UserSettings = None  # type: unique symbol

class ServiceVisibilityService:
    def __init__(self):
        self._nominal_ServiceVisibilityService = None  # type: unique symbol

class SessionService:
    def __init__(self):
        self._nominal_SessionService = None  # type: unique symbol

class SharedTableRegistry:
    def __init__(self):
        self._nominal_SharedTableRegistry = None  # type: unique symbol

class Sky:
    def __init__(self):
        self._nominal_Sky = None  # type: unique symbol

class Smoke:
    def __init__(self):
        self._nominal_Smoke = None  # type: unique symbol

class SmoothVoxelsUpgraderService:
    def __init__(self):
        self._nominal_SmoothVoxelsUpgraderService = None  # type: unique symbol

class SnippetService:
    def __init__(self):
        self._nominal_SnippetService = None  # type: unique symbol

class SocialService:
    def __init__(self):
        self._nominal_SocialService = None  # type: unique symbol

class Sound:
    def __init__(self):
        self._nominal_Sound = None  # type: unique symbol

class SoundEffect:
    def __init__(self):
        self._nominal_SoundEffect = None  # type: unique symbol

class ChorusSoundEffect:
    def __init__(self):
        self._nominal_ChorusSoundEffect = None  # type: unique symbol

class CompressorSoundEffect:
    def __init__(self):
        self._nominal_CompressorSoundEffect = None  # type: unique symbol

class CustomSoundEffect:
    def __init__(self):
        self._nominal_CustomSoundEffect = None  # type: unique symbol

class AssetSoundEffect:
    def __init__(self):
        self._nominal_AssetSoundEffect = None  # type: unique symbol

class ChannelSelectorSoundEffect:
    def __init__(self):
        self._nominal_ChannelSelectorSoundEffect = None  # type: unique symbol

class DistortionSoundEffect:
    def __init__(self):
        self._nominal_DistortionSoundEffect = None  # type: unique symbol

class EchoSoundEffect:
    def __init__(self):
        self._nominal_EchoSoundEffect = None  # type: unique symbol

class EqualizerSoundEffect:
    def __init__(self):
        self._nominal_EqualizerSoundEffect = None  # type: unique symbol

class FlangeSoundEffect:
    def __init__(self):
        self._nominal_FlangeSoundEffect = None  # type: unique symbol

class PitchShiftSoundEffect:
    def __init__(self):
        self._nominal_PitchShiftSoundEffect = None  # type: unique symbol

class ReverbSoundEffect:
    def __init__(self):
        self._nominal_ReverbSoundEffect = None  # type: unique symbol

class TremoloSoundEffect:
    def __init__(self):
        self._nominal_TremoloSoundEffect = None  # type: unique symbol

class SoundGroup:
    def __init__(self):
        self._nominal_SoundGroup = None  # type: unique symbol

class SoundService:
    def __init__(self):
        self._nominal_SoundService = None  # type: unique symbol
        self.DefaultListenerLocation = None  # type: Enum.ListenerLocation

class Sparkles:
    def __init__(self):
        self._nominal_Sparkles = None  # type: unique symbol

class StackFrame:
    def __init__(self):
        self._nominal_StackFrame = None  # type: unique symbol

class StartPageService:
    def __init__(self):
        self._nominal_StartPageService = None  # type: unique symbol

class StarterGear:
    def __init__(self):
        self._nominal_StarterGear = None  # type: unique symbol

class StarterPack:
    def __init__(self):
        self._nominal_StarterPack = None  # type: unique symbol

class StarterPlayer:
    def __init__(self):
        self._nominal_StarterPlayer = None  # type: unique symbol

class StarterPlayerScripts:
    def __init__(self):
        self._nominal_StarterPlayerScripts = None  # type: unique symbol

class StarterCharacterScripts:
    def __init__(self):
        self._nominal_StarterCharacterScripts = None  # type: unique symbol

class StartupMessageService:
    def __init__(self):
        self._nominal_StartupMessageService = None  # type: unique symbol

class Stats:
    def __init__(self):
        self._nominal_Stats = None  # type: unique symbol

class StreamingService:
    def __init__(self):
        self._nominal_StreamingService = None  # type: unique symbol

class StudioAssetService:
    def __init__(self):
        self._nominal_StudioAssetService = None  # type: unique symbol

class StudioAttachment:
    def __init__(self):
        self._nominal_StudioAttachment = None  # type: unique symbol

class StudioCallout:
    def __init__(self):
        self._nominal_StudioCallout = None  # type: unique symbol

class StudioCameraService:
    def __init__(self):
        self._nominal_StudioCameraService = None  # type: unique symbol

class StudioDeviceEmulatorService:
    def __init__(self):
        self._nominal_StudioDeviceEmulatorService = None  # type: unique symbol

class StudioObjectBase:
    def __init__(self):
        self._nominal_StudioObjectBase = None  # type: unique symbol

class StudioWidget:
    def __init__(self):
        self._nominal_StudioWidget = None  # type: unique symbol

class StudioPublishService:
    def __init__(self):
        self._nominal_StudioPublishService = None  # type: unique symbol

class StudioScriptDebugEventListener:
    def __init__(self):
        self._nominal_StudioScriptDebugEventListener = None  # type: unique symbol

class StudioSdkService:
    def __init__(self):
        self._nominal_StudioSdkService = None  # type: unique symbol

class StudioUserService:
    def __init__(self):
        self._nominal_StudioUserService = None  # type: unique symbol

class StudioWidgetsService:
    def __init__(self):
        self._nominal_StudioWidgetsService = None  # type: unique symbol

class StyleBase:
    def __init__(self):
        self._nominal_StyleBase = None  # type: unique symbol

class StyleRule:
    def __init__(self):
        self._nominal_StyleRule = None  # type: unique symbol

class StyleSheet:
    def __init__(self):
        self._nominal_StyleSheet = None  # type: unique symbol

class StyleDerive:
    def __init__(self):
        self._nominal_StyleDerive = None  # type: unique symbol

class StyleLink:
    def __init__(self):
        self._nominal_StyleLink = None  # type: unique symbol

class StylingService:
    def __init__(self):
        self._nominal_StylingService = None  # type: unique symbol

class SurfaceAppearance:
    def __init__(self):
        self._nominal_SurfaceAppearance = None  # type: unique symbol
        self.AlphaMode = None  # type: Enum.AlphaMode
        self.ColorMap = None  # type: ContentId
        self.MetalnessMap = None  # type: ContentId
        self.NormalMap = None  # type: ContentId
        self.RoughnessMap = None  # type: ContentId

class SystemThemeService:
    def __init__(self):
        self._nominal_SystemThemeService = None  # type: unique symbol

class Team:
    def __init__(self):
        self._nominal_Team = None  # type: unique symbol

class TeamCreateData:
    def __init__(self):
        self._nominal_TeamCreateData = None  # type: unique symbol

class TeamCreatePublishService:
    def __init__(self):
        self._nominal_TeamCreatePublishService = None  # type: unique symbol

class TeamCreateService:
    def __init__(self):
        self._nominal_TeamCreateService = None  # type: unique symbol

class Teams:
    def __init__(self):
        self._nominal_Teams = None  # type: unique symbol

class TelemetryService:
    def __init__(self):
        self._nominal_TelemetryService = None  # type: unique symbol

class TeleportAsyncResult:
    def __init__(self):
        self._nominal_TeleportAsyncResult = None  # type: unique symbol

class TeleportOptions:
    def __init__(self):
        self._nominal_TeleportOptions = None  # type: unique symbol

class TeleportService:
    def __init__(self):
        self._nominal_TeleportService = None  # type: unique symbol

class TemporaryCageMeshProvider:
    def __init__(self):
        self._nominal_TemporaryCageMeshProvider = None  # type: unique symbol

class TemporaryScriptService:
    def __init__(self):
        self._nominal_TemporaryScriptService = None  # type: unique symbol

class TerrainDetail:
    def __init__(self):
        self._nominal_TerrainDetail = None  # type: unique symbol
        self.ColorMap = None  # type: ContentId
        self.MetalnessMap = None  # type: ContentId
        self.NormalMap = None  # type: ContentId
        self.RoughnessMap = None  # type: ContentId

class TerrainRegion:
    def __init__(self):
        self._nominal_TerrainRegion = None  # type: unique symbol

class TestService:
    def __init__(self):
        self._nominal_TestService = None  # type: unique symbol

class TextBoxService:
    def __init__(self):
        self._nominal_TextBoxService = None  # type: unique symbol

class TextChannel:
    def __init__(self):
        self._nominal_TextChannel = None  # type: unique symbol

class TextChatCommand:
    def __init__(self):
        self._nominal_TextChatCommand = None  # type: unique symbol

class TextChatConfigurations:
    def __init__(self):
        self._nominal_TextChatConfigurations = None  # type: unique symbol

class BubbleChatConfiguration:
    def __init__(self):
        self._nominal_BubbleChatConfiguration = None  # type: unique symbol

class ChannelTabsConfiguration:
    def __init__(self):
        self._nominal_ChannelTabsConfiguration = None  # type: unique symbol

class ChatInputBarConfiguration:
    def __init__(self):
        self._nominal_ChatInputBarConfiguration = None  # type: unique symbol

class ChatWindowConfiguration:
    def __init__(self):
        self._nominal_ChatWindowConfiguration = None  # type: unique symbol

class TextChatMessage:
    def __init__(self):
        self._nominal_TextChatMessage = None  # type: unique symbol

class TextChatMessageProperties:
    def __init__(self):
        self._nominal_TextChatMessageProperties = None  # type: unique symbol

class BubbleChatMessageProperties:
    def __init__(self):
        self._nominal_BubbleChatMessageProperties = None  # type: unique symbol

class ChatWindowMessageProperties:
    def __init__(self):
        self._nominal_ChatWindowMessageProperties = None  # type: unique symbol

class TextChatService:
    def __init__(self):
        self._nominal_TextChatService = None  # type: unique symbol

class TextFilterResult:
    def __init__(self):
        self._nominal_TextFilterResult = None  # type: unique symbol

class TextFilterTranslatedResult:
    def __init__(self):
        self._nominal_TextFilterTranslatedResult = None  # type: unique symbol

class TextService:
    def __init__(self):
        self._nominal_TextService = None  # type: unique symbol

class TextSource:
    def __init__(self):
        self._nominal_TextSource = None  # type: unique symbol

class TextureGenerationPartGroup:
    def __init__(self):
        self._nominal_TextureGenerationPartGroup = None  # type: unique symbol

class TextureGenerationService:
    def __init__(self):
        self._nominal_TextureGenerationService = None  # type: unique symbol

class TextureGenerationUnwrappingRequest:
    def __init__(self):
        self._nominal_TextureGenerationUnwrappingRequest = None  # type: unique symbol

class ThreadState:
    def __init__(self):
        self._nominal_ThreadState = None  # type: unique symbol

class ToastNotificationService:
    def __init__(self):
        self._nominal_ToastNotificationService = None  # type: unique symbol

class TouchTransmitter:
    def __init__(self):
        self._nominal_TouchTransmitter = None  # type: unique symbol

class TracerService:
    def __init__(self):
        self._nominal_TracerService = None  # type: unique symbol

class TrackerLodController:
    def __init__(self):
        self._nominal_TrackerLodController = None  # type: unique symbol

class TrackerStreamAnimation:
    def __init__(self):
        self._nominal_TrackerStreamAnimation = None  # type: unique symbol

class Trail:
    def __init__(self):
        self._nominal_Trail = None  # type: unique symbol

class Translator:
    def __init__(self):
        self._nominal_Translator = None  # type: unique symbol

class TutorialService:
    def __init__(self):
        self._nominal_TutorialService = None  # type: unique symbol

class TweenBase:
    def __init__(self):
        self._nominal_TweenBase = None  # type: unique symbol

class Tween:
    def __init__(self):
        self._nominal_Tween = None  # type: unique symbol

class TweenService:
    def __init__(self):
        self._nominal_TweenService = None  # type: unique symbol

class UGCAvatarService:
    def __init__(self):
        self._nominal_UGCAvatarService = None  # type: unique symbol

class UIBase:
    def __init__(self):
        self._nominal_UIBase = None  # type: unique symbol

class UIComponent:
    def __init__(self):
        self._nominal_UIComponent = None  # type: unique symbol

class UIConstraint:
    def __init__(self):
        self._nominal_UIConstraint = None  # type: unique symbol

class UIAspectRatioConstraint:
    def __init__(self):
        self._nominal_UIAspectRatioConstraint = None  # type: unique symbol

class UISizeConstraint:
    def __init__(self):
        self._nominal_UISizeConstraint = None  # type: unique symbol

class UITextSizeConstraint:
    def __init__(self):
        self._nominal_UITextSizeConstraint = None  # type: unique symbol

class UICorner:
    def __init__(self):
        self._nominal_UICorner = None  # type: unique symbol

class UIDragDetector:
    def __init__(self):
        self._nominal_UIDragDetector = None  # type: unique symbol

class UIFlexItem:
    def __init__(self):
        self._nominal_UIFlexItem = None  # type: unique symbol

class UIGradient:
    def __init__(self):
        self._nominal_UIGradient = None  # type: unique symbol

class UILayout:
    def __init__(self):
        self._nominal_UILayout = None  # type: unique symbol

class UIGridStyleLayout:
    def __init__(self):
        self._nominal_UIGridStyleLayout = None  # type: unique symbol

class UIGridLayout:
    def __init__(self):
        self._nominal_UIGridLayout = None  # type: unique symbol

class UIListLayout:
    def __init__(self):
        self._nominal_UIListLayout = None  # type: unique symbol

class UIPageLayout:
    def __init__(self):
        self._nominal_UIPageLayout = None  # type: unique symbol

class UITableLayout:
    def __init__(self):
        self._nominal_UITableLayout = None  # type: unique symbol

class UIPadding:
    def __init__(self):
        self._nominal_UIPadding = None  # type: unique symbol

class UIScale:
    def __init__(self):
        self._nominal_UIScale = None  # type: unique symbol

class UIStroke:
    def __init__(self):
        self._nominal_UIStroke = None  # type: unique symbol

class UIDragDetectorService:
    def __init__(self):
        self._nominal_UIDragDetectorService = None  # type: unique symbol

class UniqueIdLookupService:
    def __init__(self):
        self._nominal_UniqueIdLookupService = None  # type: unique symbol

class UnvalidatedAssetService:
    def __init__(self):
        self._nominal_UnvalidatedAssetService = None  # type: unique symbol

class UserGameSettings:
    def __init__(self):
        self._nominal_UserGameSettings = None  # type: unique symbol

class UserInputService:
    def __init__(self):
        self._nominal_UserInputService = None  # type: unique symbol

class UserService:
    def __init__(self):
        self._nominal_UserService = None  # type: unique symbol

class VRService:
    def __init__(self):
        self._nominal_VRService = None  # type: unique symbol

class VRStatusService:
    def __init__(self):
        self._nominal_VRStatusService = None  # type: unique symbol

class ValueBase:
    def __init__(self):
        self._nominal_ValueBase = None  # type: unique symbol
        self.Value = None  # type: unknown
        self.Changed = None  # type: RBXScriptSignal<(value?: unknown) => void>

class BoolValue:
    def __init__(self):
        self._nominal_BoolValue = None  # type: unique symbol

class BrickColorValue:
    def __init__(self):
        self._nominal_BrickColorValue = None  # type: unique symbol

class CFrameValue:
    def __init__(self):
        self._nominal_CFrameValue = None  # type: unique symbol

class Color3Value:
    def __init__(self):
        self._nominal_Color3Value = None  # type: unique symbol

class DoubleConstrainedValue:
    def __init__(self):
        self._nominal_DoubleConstrainedValue = None  # type: unique symbol

class IntConstrainedValue:
    def __init__(self):
        self._nominal_IntConstrainedValue = None  # type: unique symbol

class IntValue:
    def __init__(self):
        self._nominal_IntValue = None  # type: unique symbol

class NumberValue:
    def __init__(self):
        self._nominal_NumberValue = None  # type: unique symbol

class ObjectValue:
    def __init__(self):
        self._nominal_ObjectValue = None  # type: unique symbol

class RayValue:
    def __init__(self):
        self._nominal_RayValue = None  # type: unique symbol

class StringValue:
    def __init__(self):
        self._nominal_StringValue = None  # type: unique symbol

class Vector3Value:
    def __init__(self):
        self._nominal_Vector3Value = None  # type: unique symbol

class Vector3Curve:
    def __init__(self):
        self._nominal_Vector3Curve = None  # type: unique symbol

class VideoCaptureService:
    def __init__(self):
        self._nominal_VideoCaptureService = None  # type: unique symbol

class VideoDeviceInput:
    def __init__(self):
        self._nominal_VideoDeviceInput = None  # type: unique symbol

class VideoPlayer:
    def __init__(self):
        self._nominal_VideoPlayer = None  # type: unique symbol

class VideoService:
    def __init__(self):
        self._nominal_VideoService = None  # type: unique symbol

class VisibilityCheckDispatcher:
    def __init__(self):
        self._nominal_VisibilityCheckDispatcher = None  # type: unique symbol

class VisualizationMode:
    def __init__(self):
        self._nominal_VisualizationMode = None  # type: unique symbol

class VisualizationModeCategory:
    def __init__(self):
        self._nominal_VisualizationModeCategory = None  # type: unique symbol

class VisualizationModeService:
    def __init__(self):
        self._nominal_VisualizationModeService = None  # type: unique symbol

class VoiceChatInternal:
    def __init__(self):
        self._nominal_VoiceChatInternal = None  # type: unique symbol

class VoiceChatService:
    def __init__(self):
        self._nominal_VoiceChatService = None  # type: unique symbol
        self.DefaultDistanceAttenuation = None  # type: Enum.VoiceChatDistanceAttenuationType
        self.EnableDefaultVoice = None  # type: bool
        self.UseAudioApi = None  # type: Enum.AudioApiRollout

class WebSocketClient:
    def __init__(self):
        self._nominal_WebSocketClient = None  # type: unique symbol

class WebSocketService:
    def __init__(self):
        self._nominal_WebSocketService = None  # type: unique symbol

class WebViewService:
    def __init__(self):
        self._nominal_WebViewService = None  # type: unique symbol

class WeldConstraint:
    def __init__(self):
        self._nominal_WeldConstraint = None  # type: unique symbol

class Wire:
    def __init__(self):
        self._nominal_Wire = None  # type: unique symbol

class CoreGui:
    def __init__(self):
        self._nominal_CoreGui = None  # type: unique symbol

class ChangeHistoryService:
    def __init__(self):
        self._nominal_ChangeHistoryService = None  # type: unique symbol
        self.OnRecordingFinished = None  # type: RBXScriptSignal<(name: str, displayName: str | undefined, identifier: str | undefined, operation: Enum.FinishRecordingOperation, finalOptions?: object) => void>
        self.OnRecordingStarted = None  # type: RBXScriptSignal<(name: str, displayName?: str) => void>
        self.OnRedo = None  # type: RBXScriptSignal<(waypoint: str) => void>
        self.OnUndo = None  # type: RBXScriptSignal<(waypoint: str) => void>

class DataModelSession:
    def __init__(self):
        self._nominal_DataModelSession = None  # type: unique symbol

class DebugSettings:
    def __init__(self):
        self._nominal_DebugSettings = None  # type: unique symbol

class DebuggerBreakpoint:
    def __init__(self):
        self._nominal_DebuggerBreakpoint = None  # type: unique symbol

class DebuggerManager:
    def __init__(self):
        self._nominal_DebuggerManager = None  # type: unique symbol

class DebuggerWatch:
    def __init__(self):
        self._nominal_DebuggerWatch = None  # type: unique symbol

class File:
    def __init__(self):
        self._nominal_File = None  # type: unique symbol
        self.Size = None  # type: float

class GameSettings:
    def __init__(self):
        self._nominal_GameSettings = None  # type: unique symbol

class PluginGui:
    def __init__(self):
        self._nominal_PluginGui = None  # type: unique symbol
        self.PluginDragDropped = None  # type: RBXScriptSignal<(dragData: object) => void>
        self.PluginDragEntered = None  # type: RBXScriptSignal<(dragData: object) => void>
        self.PluginDragLeft = None  # type: RBXScriptSignal<(dragData: object) => void>
        self.PluginDragMoved = None  # type: RBXScriptSignal<(dragData: object) => void>
        self.WindowFocusReleased = None  # type: RBXScriptSignal<() => void>
        self.WindowFocused = None  # type: RBXScriptSignal<() => void>

class DockWidgetPluginGui:
    def __init__(self):
        self._nominal_DockWidgetPluginGui = None  # type: unique symbol

class QWidgetPluginGui:
    def __init__(self):
        self._nominal_QWidgetPluginGui = None  # type: unique symbol

class LuaSettings:
    def __init__(self):
        self._nominal_LuaSettings = None  # type: unique symbol

class MemStorageConnection:
    def __init__(self):
        self._nominal_MemStorageConnection = None  # type: unique symbol

class PluginMouse:
    def __init__(self):
        self._nominal_PluginMouse = None  # type: unique symbol
        self.DragEnter = None  # type: RBXScriptSignal<(instances: List(Instance)) => void>

class MultipleDocumentInterfaceInstance:
    def __init__(self):
        self._nominal_MultipleDocumentInterfaceInstance = None  # type: unique symbol

class NetworkPeer:
    def __init__(self):
        self._nominal_NetworkPeer = None  # type: unique symbol

class NetworkClient:
    def __init__(self):
        self._nominal_NetworkClient = None  # type: unique symbol

class NetworkServer:
    def __init__(self):
        self._nominal_NetworkServer = None  # type: unique symbol

class NetworkReplicator:
    def __init__(self):
        self._nominal_NetworkReplicator = None  # type: unique symbol

class ClientReplicator:
    def __init__(self):
        self._nominal_ClientReplicator = None  # type: unique symbol

class ServerReplicator:
    def __init__(self):
        self._nominal_ServerReplicator = None  # type: unique symbol

class NetworkSettings:
    def __init__(self):
        self._nominal_NetworkSettings = None  # type: unique symbol
        self.EmulatedTotalMemoryInMB = None  # type: float
        self.FreeMemoryMBytes = None  # type: float

class PackageService:
    def __init__(self):
        self._nominal_PackageService = None  # type: unique symbol

class PhysicsSettings:
    def __init__(self):
        self._nominal_PhysicsSettings = None  # type: unique symbol

class Plugin:
    def __init__(self):
        self._nominal_Plugin = None  # type: unique symbol
        self.Deactivation = None  # type: RBXScriptSignal<() => void>
        self.Unloading = None  # type: RBXScriptSignal<() => void>

class PluginAction:
    def __init__(self):
        self._nominal_PluginAction = None  # type: unique symbol
        self.Triggered = None  # type: RBXScriptSignal<() => void>

class PluginDebugService:
    def __init__(self):
        self._nominal_PluginDebugService = None  # type: unique symbol

class PluginDragEvent:
    def __init__(self):
        self._nominal_PluginDragEvent = None  # type: unique symbol

class PluginGuiService:
    def __init__(self):
        self._nominal_PluginGuiService = None  # type: unique symbol

class PluginMenu:
    def __init__(self):
        self._nominal_PluginMenu = None  # type: unique symbol

class PluginToolbar:
    def __init__(self):
        self._nominal_PluginToolbar = None  # type: unique symbol

class PluginToolbarButton:
    def __init__(self):
        self._nominal_PluginToolbarButton = None  # type: unique symbol
        self.Click = None  # type: RBXScriptSignal<() => void>

class RenderSettings:
    def __init__(self):
        self._nominal_RenderSettings = None  # type: unique symbol

class RenderingTest:
    def __init__(self):
        self._nominal_RenderingTest = None  # type: unique symbol

class RobloxPluginGuiService:
    def __init__(self):
        self._nominal_RobloxPluginGuiService = None  # type: unique symbol

class ScriptDebugger:
    def __init__(self):
        self._nominal_ScriptDebugger = None  # type: unique symbol

class ScriptDocument:
    def __init__(self):
        self._nominal_ScriptDocument = None  # type: unique symbol
        self.SelectionChanged = None  # type: RBXScriptSignal<(positionLine: float, positionCharacter: float, anchorLine: float, anchorCharacter: float) => void>
        self.ViewportChanged = None  # type: RBXScriptSignal<(startLine: float, endLine: float) => void>

class ScriptEditorService:
    def __init__(self):
        self._nominal_ScriptEditorService = None  # type: unique symbol
        self.TextDocumentDidChange = None  # type: RBXScriptSignal<(document: ScriptDocument, changesArray: unknown) => void>
        self.TextDocumentDidClose = None  # type: RBXScriptSignal<(oldDocument: ScriptDocument) => void>
        self.TextDocumentDidOpen = None  # type: RBXScriptSignal<(newDocument: ScriptDocument) => void>

class Selection:
    def __init__(self):
        self._nominal_Selection = None  # type: unique symbol

class GlobalSettings:
    def __init__(self):
        self._nominal_GlobalSettings = None  # type: unique symbol

class StatsItem:
    def __init__(self):
        self._nominal_StatsItem = None  # type: unique symbol
        self.DisplayName = None  # type: str

class RunningAverageItemDouble:
    def __init__(self):
        self._nominal_RunningAverageItemDouble = None  # type: unique symbol

class RunningAverageItemInt:
    def __init__(self):
        self._nominal_RunningAverageItemInt = None  # type: unique symbol

class RunningAverageTimeIntervalItem:
    def __init__(self):
        self._nominal_RunningAverageTimeIntervalItem = None  # type: unique symbol

class TotalCountTimeIntervalItem:
    def __init__(self):
        self._nominal_TotalCountTimeIntervalItem = None  # type: unique symbol

class Studio:
    def __init__(self):
        self._nominal_Studio = None  # type: unique symbol
        self.ThemeChanged = None  # type: RBXScriptSignal<() => void>

class StudioData:
    def __init__(self):
        self._nominal_StudioData = None  # type: unique symbol

class StudioService:
    def __init__(self):
        self._nominal_StudioService = None  # type: unique symbol

class StudioTheme:
    def __init__(self):
        self._nominal_StudioTheme = None  # type: unique symbol

class TaskScheduler:
    def __init__(self):
        self._nominal_TaskScheduler = None  # type: unique symbol

class VersionControlService:
    def __init__(self):
        self._nominal_VersionControlService = None  # type: unique symbol
