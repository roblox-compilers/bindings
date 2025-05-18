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
        self.CoreScriptDebuggingManagerHelper = None  # type: CoreScriptDebuggingManagerHelper
        self.CreationDBService = None  # type: CreationDBService
        self.CreatorStoreService = None  # type: CreatorStoreService
        self.CrossDMScriptChangeListener = None  # type: CrossDMScriptChangeListener
        self.DataModelPatchService = None  # type: DataModelPatchService
        self.DataStoreService = None  # type: DataStoreService
        self.Debris = None  # type: Debris
        self.DebuggablePluginWatcher = None  # type: DebuggablePluginWatcher
        self.DebuggerConnectionManager = None  # type: DebuggerConnectionManager
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
        self.OmniRecommendationsService = None  # type: OmniRecommendationsService
        self.OpenCloudService = None  # type: OpenCloudService
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
        self.PluginManagementService = None  # type: PluginManagementService
        self.PluginPolicyService = None  # type: PluginPolicyService
        self.PolicyService = None  # type: PolicyService
        self.ProcessInstancePhysicsService = None  # type: ProcessInstancePhysicsService
        self.ProximityPromptService = None  # type: ProximityPromptService
        self.PublishService = None  # type: PublishService
        self.ReflectionService = None  # type: ReflectionService
        self.RemoteCursorService = None  # type: RemoteCursorService
        self.RemoteDebuggerServer = None  # type: RemoteDebuggerServer
        self.ReplicatedFirst = None  # type: ReplicatedFirst
        self.ReplicatedStorage = None  # type: ReplicatedStorage
        self.RibbonNotificationService = None  # type: RibbonNotificationService
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
        self.ScriptProfilerService = None  # type: ScriptProfilerService
        self.ScriptRegistrationService = None  # type: ScriptRegistrationService
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
        self.StudioAssetService = None  # type: StudioAssetService
        self.StudioCameraService = None  # type: StudioCameraService
        self.StudioDeviceEmulatorService = None  # type: StudioDeviceEmulatorService
        self.StudioPublishService = None  # type: StudioPublishService
        self.StudioScriptDebugEventListener = None  # type: StudioScriptDebugEventListener
        self.StudioSdkService = None  # type: StudioSdkService
        self.StudioUserService = None  # type: StudioUserService
        self.StudioWidgetsService = None  # type: StudioWidgetsService
        self.StylingService = None  # type: StylingService
        self.SystemThemeService = None  # type: SystemThemeService
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
        self.PluginCapabilities = None  # type: PluginCapabilities
        self.PointLight = None  # type: PointLight
        self.Pose = None  # type: Pose
        self.PrismaticConstraint = None  # type: PrismaticConstraint
        self.ProximityPrompt = None  # type: ProximityPrompt
        self.RayValue = None  # type: RayValue
        self.RelativeGui = None  # type: RelativeGui
        self.RemoteEvent = None  # type: RemoteEvent
        self.RemoteFunction = None  # type: RemoteFunction
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
        self.DataStore = None  # type: DataStore
        self.DataStoreInfo = None  # type: DataStoreInfo
        self.DataStoreKey = None  # type: DataStoreKey
        self.DataStoreKeyInfo = None  # type: DataStoreKeyInfo
        self.DataStoreKeyPages = None  # type: DataStoreKeyPages
        self.DataStoreListingPages = None  # type: DataStoreListingPages
        self.DataStoreObjectVersionInfo = None  # type: DataStoreObjectVersionInfo
        self.DataStorePages = None  # type: DataStorePages
        self.DataStoreVersionPages = None  # type: DataStoreVersionPages
        self.DebuggerConnection = None  # type: DebuggerConnection
        self.DebuggerLuaResponse = None  # type: DebuggerLuaResponse
        self.DebuggerVariable = None  # type: DebuggerVariable
        self.DynamicRotate = None  # type: DynamicRotate
        self.EmotesPages = None  # type: EmotesPages
        self.ExplorerFilterAutocompleter = None  # type: ExplorerFilterAutocompleter
        self.FaceInstance = None  # type: FaceInstance
        self.FacialAnimationStreamingServiceStats = None  # type: FacialAnimationStreamingServiceStats
        self.FacialAnimationStreamingSubsessionStats = None  # type: FacialAnimationStreamingSubsessionStats
        self.FacsImportData = None  # type: FacsImportData
        self.Feature = None  # type: Feature
        self.FeedPages = None  # type: FeedPages
        self.FormFactorPart = None  # type: FormFactorPart
        self.FriendPages = None  # type: FriendPages
        self.GenericSettings = None  # type: GenericSettings
        self.GlobalDataStore = None  # type: GlobalDataStore
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
        self.LuaSourceContainer = None  # type: LuaSourceContainer
        self.ManualSurfaceJointInstance = None  # type: ManualSurfaceJointInstance
        self.MaterialGenerationSession = None  # type: MaterialGenerationSession
        self.MaterialImportData = None  # type: MaterialImportData
        self.MemoryStoreHashMap = None  # type: MemoryStoreHashMap
        self.MemoryStoreHashMapPages = None  # type: MemoryStoreHashMapPages
        self.MemoryStoreQueue = None  # type: MemoryStoreQueue
        self.MemoryStoreSortedMap = None  # type: MemoryStoreSortedMap
        self.MeshImportData = None  # type: MeshImportData
        self.MessageBusConnection = None  # type: MessageBusConnection
        self.MetaBreakpoint = None  # type: MetaBreakpoint
        self.MetaBreakpointContext = None  # type: MetaBreakpointContext
        self.Mouse = None  # type: Mouse
        self.NetworkMarker = None  # type: NetworkMarker
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
        self.Platform = None  # type: Platform
        self.Player = None  # type: Player
        self.PlayerData = None  # type: PlayerData
        self.PlayerDataRecord = None  # type: PlayerDataRecord
        self.PlayerDataRecordConfig = None  # type: PlayerDataRecordConfig
        self.PlayerGui = None  # type: PlayerGui
        self.PlayerMouse = None  # type: PlayerMouse
        self.PlayerScripts = None  # type: PlayerScripts
        self.PluginManagerInterface = None  # type: PluginManagerInterface
        self.PoseBase = None  # type: PoseBase
        self.PostEffect = None  # type: PostEffect
        self.PVAdornment = None  # type: PVAdornment
        self.PVInstance = None  # type: PVInstance
        self.RobloxSerializableInstance = None  # type: RobloxSerializableInstance
        self.RootImportData = None  # type: RootImportData
        self.ScreenshotHud = None  # type: ScreenshotHud
        self.ScriptBuilder = None  # type: ScriptBuilder
        self.ScriptRuntime = None  # type: ScriptRuntime
        self.SelectionLasso = None  # type: SelectionLasso
        self.SensorBase = None  # type: SensorBase
        self.ServiceProvider = None  # type: ServiceProvider
        self.SlidingBallConstraint = None  # type: SlidingBallConstraint
        self.SoundEffect = None  # type: SoundEffect
        self.StackFrame = None  # type: StackFrame
        self.StandardPages = None  # type: StandardPages
        self.StarterCharacterScripts = None  # type: StarterCharacterScripts
        self.StarterPlayerScripts = None  # type: StarterPlayerScripts
        self.StudioObjectBase = None  # type: StudioObjectBase
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
        self.ClassName = None  # type: str
        self.Changed = None  # type: unknown

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
        self.Error = None  # type: Enum.ConfigSnapshotErrorState
        self.Outdated = None  # type: bool
        self.UpdateAvailable = None  # type: RBXScriptSignal<() => void>

class EditableImage:
    def __init__(self):
        self._nominal_EditableImage = None  # type: unique symbol
        self.Size = None  # type: Vector2

class EditableMesh:
    def __init__(self):
        self._nominal_EditableMesh = None  # type: unique symbol
        self.SkinningEnabled = None  # type: bool

class Instance:
    def __init__(self):
        self._nominal_Instance = None  # type: unique symbol
        self.Archivable = None  # type: bool
        self.Capabilities = None  # type: SecurityCapabilities
        self.Name = None  # type: str
        self.Parent = None  # type: Instance | undefined
        self.Sandboxed = None  # type: bool
        self.AncestryChanged = None  # type: RBXScriptSignal<(child: Instance, parent: Instance | undefined) => void>
        self.AttributeChanged = None  # type: RBXScriptSignal<(attribute: str) => void>
        self.ChildAdded = None  # type: RBXScriptSignal<(child: Instance) => void>
        self.ChildRemoved = None  # type: RBXScriptSignal<(child: Instance) => void>
        self.DescendantAdded = None  # type: RBXScriptSignal<(descendant: Instance) => void>
        self.DescendantRemoving = None  # type: RBXScriptSignal<(descendant: Instance) => void>
        self.Destroying = None  # type: RBXScriptSignal<() => void>
        self.StyledPropertiesChanged = None  # type: RBXScriptSignal<() => void>

class AccessoryDescription:
    def __init__(self):
        self._nominal_AccessoryDescription = None  # type: unique symbol
        self.AccessoryType = None  # type: Enum.AccessoryType
        self.AssetId = None  # type: float
        self.Instance = None  # type: Instance | undefined
        self.IsLayered = None  # type: bool
        self.Order = None  # type: float
        self.Position = None  # type: Vector3
        self.Puffiness = None  # type: float
        self.Rotation = None  # type: Vector3
        self.Scale = None  # type: Vector3

class AccountService:
    def __init__(self):
        self._nominal_AccountService = None  # type: unique symbol

class Accoutrement:
    def __init__(self):
        self._nominal_Accoutrement = None  # type: unique symbol
        self.AttachmentForward = None  # type: Vector3
        self.AttachmentPoint = None  # type: CFrame
        self.AttachmentPos = None  # type: Vector3
        self.AttachmentRight = None  # type: Vector3
        self.AttachmentUp = None  # type: Vector3

class Accessory:
    def __init__(self):
        self._nominal_Accessory = None  # type: unique symbol
        self.AccessoryType = None  # type: Enum.AccessoryType

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
        self.Status = None  # type: Enum.AdUnitStatus

class AnalyticsService:
    def __init__(self):
        self._nominal_AnalyticsService = None  # type: unique symbol

class Animation:
    def __init__(self):
        self._nominal_Animation = None  # type: unique symbol
        self.AnimationId = None  # type: ContentId

class AnimationClip:
    def __init__(self):
        self._nominal_AnimationClip = None  # type: unique symbol
        self.Loop = None  # type: bool
        self.Priority = None  # type: Enum.AnimationPriority

class CurveAnimation:
    def __init__(self):
        self._nominal_CurveAnimation = None  # type: unique symbol

class KeyframeSequence:
    def __init__(self):
        self._nominal_KeyframeSequence = None  # type: unique symbol

class AnimationClipProvider:
    def __init__(self):
        self._nominal_AnimationClipProvider = None  # type: unique symbol

class AnimationController:
    def __init__(self):
        self._nominal_AnimationController = None  # type: unique symbol
        self.AnimationPlayed = None  # type: RBXScriptSignal<(animationTrack: AnimationTrack) => void>

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
        self.Animation = None  # type: TrackerStreamAnimation | undefined
        self.FACSDataLod = None  # type: Enum.FACSDataLod
        self.IsPlaying = None  # type: bool
        self.Priority = None  # type: Enum.AnimationPriority
        self.WeightCurrent = None  # type: float
        self.WeightTarget = None  # type: float

class AnimationTrack:
    def __init__(self):
        self._nominal_AnimationTrack = None  # type: unique symbol
        self.Animation = None  # type: Animation | undefined
        self.IsPlaying = None  # type: bool
        self.Length = None  # type: float
        self.Looped = None  # type: bool
        self.Priority = None  # type: Enum.AnimationPriority
        self.Speed = None  # type: float
        self.TimePosition = None  # type: float
        self.WeightCurrent = None  # type: float
        self.WeightTarget = None  # type: float
        self.DidLoop = None  # type: RBXScriptSignal<() => void>
        self.Ended = None  # type: RBXScriptSignal<() => void>
        self.KeyframeReached = None  # type: RBXScriptSignal<(keyframeName: str) => void>
        self.Stopped = None  # type: RBXScriptSignal<() => void>

class Animator:
    def __init__(self):
        self._nominal_Animator = None  # type: unique symbol
        self.EvaluationThrottled = None  # type: bool
        self.PreferLodEnabled = None  # type: bool
        self.RootMotion = None  # type: CFrame
        self.RootMotionWeight = None  # type: float
        self.AnimationPlayed = None  # type: RBXScriptSignal<(animationTrack: AnimationTrack) => void>

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
        self.Interface = None  # type: str
        self.Port = None  # type: float
        self.StartServer = None  # type: bool

class AssetImportService:
    def __init__(self):
        self._nominal_AssetImportService = None  # type: unique symbol

class AssetManagerService:
    def __init__(self):
        self._nominal_AssetManagerService = None  # type: unique symbol

class AssetPatchSettings:
    def __init__(self):
        self._nominal_AssetPatchSettings = None  # type: unique symbol
        self.ContentId = None  # type: str
        self.OutputPath = None  # type: str
        self.PatchId = None  # type: str

class AssetService:
    def __init__(self):
        self._nominal_AssetService = None  # type: unique symbol

class Atmosphere:
    def __init__(self):
        self._nominal_Atmosphere = None  # type: unique symbol
        self.Color = None  # type: Color3
        self.Decay = None  # type: Color3
        self.Density = None  # type: float
        self.Glare = None  # type: float
        self.Haze = None  # type: float
        self.Offset = None  # type: float

class Attachment:
    def __init__(self):
        self._nominal_Attachment = None  # type: unique symbol
        self.Axis = None  # type: Vector3
        self.CFrame = None  # type: CFrame
        self.Orientation = None  # type: Vector3
        self.Position = None  # type: Vector3
        self.Rotation = None  # type: Vector3
        self.SecondaryAxis = None  # type: Vector3
        self.Visible = None  # type: bool
        self.WorldAxis = None  # type: Vector3
        self.WorldCFrame = None  # type: CFrame
        self.WorldOrientation = None  # type: Vector3
        self.WorldPosition = None  # type: Vector3
        self.WorldRotation = None  # type: Vector3
        self.WorldSecondaryAxis = None  # type: Vector3

class Bone:
    def __init__(self):
        self._nominal_Bone = None  # type: unique symbol
        self.Transform = None  # type: CFrame
        self.TransformedCFrame = None  # type: CFrame
        self.TransformedWorldCFrame = None  # type: CFrame

class AudioAnalyzer:
    def __init__(self):
        self._nominal_AudioAnalyzer = None  # type: unique symbol
        self.PeakLevel = None  # type: float
        self.RmsLevel = None  # type: float
        self.SpectrumEnabled = None  # type: bool
        self.WindowSize = None  # type: Enum.AudioWindowSize
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioChannelMixer:
    def __init__(self):
        self._nominal_AudioChannelMixer = None  # type: unique symbol
        self.Layout = None  # type: Enum.AudioChannelLayout
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioChannelSplitter:
    def __init__(self):
        self._nominal_AudioChannelSplitter = None  # type: unique symbol
        self.Layout = None  # type: Enum.AudioChannelLayout
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioChorus:
    def __init__(self):
        self._nominal_AudioChorus = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.Depth = None  # type: float
        self.Mix = None  # type: float
        self.Rate = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioCompressor:
    def __init__(self):
        self._nominal_AudioCompressor = None  # type: unique symbol
        self.Attack = None  # type: float
        self.Bypass = None  # type: bool
        self.MakeupGain = None  # type: float
        self.Ratio = None  # type: float
        self.Release = None  # type: float
        self.Threshold = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioDeviceInput:
    def __init__(self):
        self._nominal_AudioDeviceInput = None  # type: unique symbol
        self.AccessType = None  # type: Enum.AccessModifierType
        self.Muted = None  # type: bool
        self.Player = None  # type: Player | undefined
        self.Volume = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioDeviceOutput:
    def __init__(self):
        self._nominal_AudioDeviceOutput = None  # type: unique symbol
        self.Player = None  # type: Player | undefined
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioDistortion:
    def __init__(self):
        self._nominal_AudioDistortion = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.Level = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioEcho:
    def __init__(self):
        self._nominal_AudioEcho = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.DelayTime = None  # type: float
        self.DryLevel = None  # type: float
        self.Feedback = None  # type: float
        self.RampTime = None  # type: float
        self.WetLevel = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioEmitter:
    def __init__(self):
        self._nominal_AudioEmitter = None  # type: unique symbol
        self.AudioInteractionGroup = None  # type: str
        self.SimulationFidelity = None  # type: Enum.AudioSimulationFidelity
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioEqualizer:
    def __init__(self):
        self._nominal_AudioEqualizer = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.HighGain = None  # type: float
        self.LowGain = None  # type: float
        self.MidGain = None  # type: float
        self.MidRange = None  # type: NumberRange
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioFader:
    def __init__(self):
        self._nominal_AudioFader = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.Volume = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioFilter:
    def __init__(self):
        self._nominal_AudioFilter = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.FilterType = None  # type: Enum.AudioFilterType
        self.Frequency = None  # type: float
        self.Gain = None  # type: float
        self.Q = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioFlanger:
    def __init__(self):
        self._nominal_AudioFlanger = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.Depth = None  # type: float
        self.Mix = None  # type: float
        self.Rate = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioFocusService:
    def __init__(self):
        self._nominal_AudioFocusService = None  # type: unique symbol

class AudioLimiter:
    def __init__(self):
        self._nominal_AudioLimiter = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.MaxLevel = None  # type: float
        self.Release = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioListener:
    def __init__(self):
        self._nominal_AudioListener = None  # type: unique symbol
        self.AudioInteractionGroup = None  # type: str
        self.SimulationFidelity = None  # type: Enum.AudioSimulationFidelity
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioPitchShifter:
    def __init__(self):
        self._nominal_AudioPitchShifter = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.Pitch = None  # type: float
        self.WindowSize = None  # type: Enum.AudioWindowSize
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioPlayer:
    def __init__(self):
        self._nominal_AudioPlayer = None  # type: unique symbol
        self.Asset = None  # type: ContentId
        self.AssetId = None  # type: str
        self.AutoLoad = None  # type: bool
        self.IsReady = None  # type: bool
        self.LoopRegion = None  # type: NumberRange
        self.Looping = None  # type: bool
        self.PlaybackRegion = None  # type: NumberRange
        self.PlaybackSpeed = None  # type: float
        self.TimeLength = None  # type: float
        self.TimePosition = None  # type: float
        self.Volume = None  # type: float
        self.Ended = None  # type: RBXScriptSignal<() => void>
        self.Looped = None  # type: RBXScriptSignal<() => void>
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioRecorder:
    def __init__(self):
        self._nominal_AudioRecorder = None  # type: unique symbol
        self.TimeLength = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioReverb:
    def __init__(self):
        self._nominal_AudioReverb = None  # type: unique symbol
        self.Bypass = None  # type: bool
        self.DecayRatio = None  # type: float
        self.DecayTime = None  # type: float
        self.Density = None  # type: float
        self.Diffusion = None  # type: float
        self.DryLevel = None  # type: float
        self.EarlyDelayTime = None  # type: float
        self.HighCutFrequency = None  # type: float
        self.LateDelayTime = None  # type: float
        self.LowShelfFrequency = None  # type: float
        self.LowShelfGain = None  # type: float
        self.ReferenceFrequency = None  # type: float
        self.WetLevel = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AudioSearchParams:
    def __init__(self):
        self._nominal_AudioSearchParams = None  # type: unique symbol
        self.Album = None  # type: str
        self.Artist = None  # type: str
        self.AudioSubType = None  # type: Enum.AudioSubType
        self.AudioSubtype = None  # type: Enum.AudioSubType
        self.MaxDuration = None  # type: float
        self.MinDuration = None  # type: float
        self.SearchKeyword = None  # type: str
        self.Tag = None  # type: str
        self.Title = None  # type: str

class AudioTextToSpeech:
    def __init__(self):
        self._nominal_AudioTextToSpeech = None  # type: unique symbol
        self.IsLoaded = None  # type: bool
        self.Looping = None  # type: bool
        self.Pitch = None  # type: float
        self.PlaybackSpeed = None  # type: float
        self.Speed = None  # type: float
        self.Text = None  # type: str
        self.TimeLength = None  # type: float
        self.TimePosition = None  # type: float
        self.VoiceId = None  # type: str
        self.Volume = None  # type: float
        self.Ended = None  # type: RBXScriptSignal<() => void>
        self.Looped = None  # type: RBXScriptSignal<() => void>
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class AuroraScriptObject:
    def __init__(self):
        self._nominal_AuroraScriptObject = None  # type: unique symbol
        self.FrameId = None  # type: float

class AuroraScriptService:
    def __init__(self):
        self._nominal_AuroraScriptService = None  # type: unique symbol

class AuroraService:
    def __init__(self):
        self._nominal_AuroraService = None  # type: unique symbol
        self.HashRoundingPoint = None  # type: float
        self.IgnoreRotation = None  # type: bool
        self.RollbackOffset = None  # type: float
        self.FixedRateTick = None  # type: RBXScriptSignal<(deltaTime: float, worldStepId: float) => void>
        self.Misprediction = None  # type: RBXScriptSignal<(worldStepId: float, mispredictedInstances: List(unknown)) => void>
        self.Rollback = None  # type: RBXScriptSignal<(worldStepId: float) => void>
        self.Step = None  # type: RBXScriptSignal<() => void>

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
        self.AvatarModerationCompleted = None  # type: RBXScriptSignal<(outfitId: float, moderationStatus: Enum.ModerationStatus) => void>

class AvatarEditorService:
    def __init__(self):
        self._nominal_AvatarEditorService = None  # type: unique symbol
        self.PromptAllowInventoryReadAccessCompleted = None  # type: RBXScriptSignal<(result: Enum.AvatarPromptResult) => void>
        self.PromptCreateOutfitCompleted = None  # type: RBXScriptSignal<(result: Enum.AvatarPromptResult, failureType: unknown) => void>
        self.PromptDeleteOutfitCompleted = None  # type: RBXScriptSignal<(result: Enum.AvatarPromptResult) => void>
        self.PromptRenameOutfitCompleted = None  # type: RBXScriptSignal<(result: Enum.AvatarPromptResult) => void>
        self.PromptSaveAvatarCompleted = None  # type: RBXScriptSignal<(result: Enum.AvatarPromptResult, humanoidDescription: HumanoidDescription) => void>
        self.PromptSetFavoriteCompleted = None  # type: RBXScriptSignal<(result: Enum.AvatarPromptResult) => void>
        self.PromptUpdateOutfitCompleted = None  # type: RBXScriptSignal<(result: Enum.AvatarPromptResult) => void>

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
        self.Id = None  # type: str
        self.ImportName = None  # type: str
        self.ShouldImport = None  # type: bool
        self.StatusRemoved = None  # type: RBXScriptSignal<(status: object) => void>
        self.StatusReported = None  # type: RBXScriptSignal<(status: object) => void>

class AnimationImportData:
    def __init__(self):
        self._nominal_AnimationImportData = None  # type: unique symbol

class FacsImportData:
    def __init__(self):
        self._nominal_FacsImportData = None  # type: unique symbol

class GroupImportData:
    def __init__(self):
        self._nominal_GroupImportData = None  # type: unique symbol
        self.Anchored = None  # type: bool
        self.ImportAsModelAsset = None  # type: bool
        self.InsertInWorkspace = None  # type: bool

class JointImportData:
    def __init__(self):
        self._nominal_JointImportData = None  # type: unique symbol

class MaterialImportData:
    def __init__(self):
        self._nominal_MaterialImportData = None  # type: unique symbol
        self.DiffuseFilePath = None  # type: str
        self.IsPbr = None  # type: bool
        self.MetalnessFilePath = None  # type: str
        self.NormalFilePath = None  # type: str
        self.RoughnessFilePath = None  # type: str

class MeshImportData:
    def __init__(self):
        self._nominal_MeshImportData = None  # type: unique symbol
        self.Anchored = None  # type: bool
        self.CageManifold = None  # type: bool
        self.CageMeshIntersectedPreview = None  # type: bool
        self.CageMeshNotIntersected = None  # type: bool
        self.CageNoOverlappingVertices = None  # type: bool
        self.CageNonManifoldPreview = None  # type: bool
        self.CageOverlappingVerticesPreview = None  # type: bool
        self.CageUVMatched = None  # type: bool
        self.CageUVMisMatchedPreview = None  # type: bool
        self.Dimensions = None  # type: Vector3
        self.DoubleSided = None  # type: bool
        self.IgnoreVertexColors = None  # type: bool
        self.IrrelevantCageModifiedPreview = None  # type: bool
        self.MeshHoleDetectedPreview = None  # type: bool
        self.MeshNoHoleDetected = None  # type: bool
        self.NoIrrelevantCageModified = None  # type: bool
        self.NoOuterCageFarExtendedFromMesh = None  # type: bool
        self.OuterCageFarExtendedFromMeshPreview = None  # type: bool
        self.PolygonCount = None  # type: float
        self.UseImportedPivot = None  # type: bool

class RootImportData:
    def __init__(self):
        self._nominal_RootImportData = None  # type: unique symbol
        self.AddModelToInventory = None  # type: bool
        self.Anchored = None  # type: bool
        self.AnimationIdForRestPose = None  # type: float
        self.ExistingPackageId = None  # type: str
        self.FileDimensions = None  # type: Vector3
        self.ImportAsModelAsset = None  # type: bool
        self.ImportAsPackage = None  # type: bool
        self.InsertInWorkspace = None  # type: bool
        self.InsertWithScenePosition = None  # type: bool
        self.InvertNegativeFaces = None  # type: bool
        self.KeepZeroInfluenceBones = None  # type: bool
        self.MergeMeshes = None  # type: bool
        self.PolygonCount = None  # type: float
        self.PreferredUploadId = None  # type: float
        self.RestPose = None  # type: Enum.RestPose
        self.RigScale = None  # type: Enum.RigScale
        self.RigType = None  # type: Enum.RigType
        self.RigVisualization = None  # type: bool
        self.ScaleUnit = None  # type: Enum.MeshScaleUnit
        self.UseSceneOriginAsPivot = None  # type: bool
        self.UsesCages = None  # type: bool
        self.ValidateUgcBody = None  # type: bool
        self.WorldForward = None  # type: Enum.NormalId
        self.WorldUp = None  # type: Enum.NormalId

class BasePlayerGui:
    def __init__(self):
        self._nominal_BasePlayerGui = None  # type: unique symbol

class PlayerGui:
    def __init__(self):
        self._nominal_PlayerGui = None  # type: unique symbol
        self.CurrentScreenOrientation = None  # type: Enum.ScreenOrientation
        self.ScreenOrientation = None  # type: Enum.ScreenOrientation
        self.SelectionImageObject = None  # type: GuiObject | undefined
        self.TopbarTransparencyChangedSignal = None  # type: RBXScriptSignal<(transparency: float) => void>

class StarterGui:
    def __init__(self):
        self._nominal_StarterGui = None  # type: unique symbol
        self.ResetPlayerGuiOnSpawn = None  # type: bool
        self.ScreenOrientation = None  # type: Enum.ScreenOrientation
        self.ShowDevelopmentGui = None  # type: bool

class BaseRemoteEvent:
    def __init__(self):
        self._nominal_BaseRemoteEvent = None  # type: unique symbol

class RemoteEvent:
    def __init__(self):
        self._nominal_RemoteEvent = None  # type: unique symbol
        self.OnClientEvent = None  # type: RBXScriptSignal<T>
        self.OnServerEvent = None  # type: RBXScriptSignal<(player: Player, ...args: List(unknown)) => void>

class UnreliableRemoteEvent:
    def __init__(self):
        self._nominal_UnreliableRemoteEvent = None  # type: unique symbol
        self.OnClientEvent = None  # type: RBXScriptSignal<T>
        self.OnServerEvent = None  # type: RBXScriptSignal<(player: Player, ...args: List(unknown)) => void>

class BaseWrap:
    def __init__(self):
        self._nominal_BaseWrap = None  # type: unique symbol
        self.CageOriginWorld = None  # type: CFrame
        self.ImportOriginWorld = None  # type: CFrame

class WrapDeformer:
    def __init__(self):
        self._nominal_WrapDeformer = None  # type: unique symbol

class WrapLayer:
    def __init__(self):
        self._nominal_WrapLayer = None  # type: unique symbol
        self.AutoSkin = None  # type: Enum.WrapLayerAutoSkin
        self.Enabled = None  # type: bool
        self.Order = None  # type: float
        self.Puffiness = None  # type: float
        self.ReferenceOriginWorld = None  # type: CFrame

class WrapTarget:
    def __init__(self):
        self._nominal_WrapTarget = None  # type: unique symbol

class Beam:
    def __init__(self):
        self._nominal_Beam = None  # type: unique symbol
        self.Attachment0 = None  # type: Attachment | undefined
        self.Attachment1 = None  # type: Attachment | undefined
        self.Brightness = None  # type: float
        self.Color = None  # type: ColorSequence
        self.CurveSize0 = None  # type: float
        self.CurveSize1 = None  # type: float
        self.Enabled = None  # type: bool
        self.FaceCamera = None  # type: bool
        self.LightEmission = None  # type: float
        self.LightInfluence = None  # type: float
        self.LocalTransparencyModifier = None  # type: float
        self.Segments = None  # type: float
        self.Texture = None  # type: ContentId
        self.TextureLength = None  # type: float
        self.TextureMode = None  # type: Enum.TextureMode
        self.TextureSpeed = None  # type: float
        self.Transparency = None  # type: NumberSequence
        self.Width0 = None  # type: float
        self.Width1 = None  # type: float
        self.ZOffset = None  # type: float

class BindableEvent:
    def __init__(self):
        self._nominal_BindableEvent = None  # type: unique symbol
        self.Event = None  # type: RBXScriptSignal<T>

class BindableFunction:
    def __init__(self):
        self._nominal_BindableFunction = None  # type: unique symbol
        self.OnInvoke = None  # type: T | undefined

class BodyMover:
    def __init__(self):
        self._nominal_BodyMover = None  # type: unique symbol

class BodyAngularVelocity:
    def __init__(self):
        self._nominal_BodyAngularVelocity = None  # type: unique symbol
        self.AngularVelocity = None  # type: Vector3
        self.MaxTorque = None  # type: Vector3
        self.P = None  # type: float

class BodyForce:
    def __init__(self):
        self._nominal_BodyForce = None  # type: unique symbol
        self.Force = None  # type: Vector3

class BodyGyro:
    def __init__(self):
        self._nominal_BodyGyro = None  # type: unique symbol
        self.CFrame = None  # type: CFrame
        self.D = None  # type: float
        self.MaxTorque = None  # type: Vector3
        self.P = None  # type: float

class BodyPosition:
    def __init__(self):
        self._nominal_BodyPosition = None  # type: unique symbol
        self.D = None  # type: float
        self.MaxForce = None  # type: Vector3
        self.P = None  # type: float
        self.Position = None  # type: Vector3
        self.ReachedTarget = None  # type: RBXScriptSignal<() => void>

class BodyThrust:
    def __init__(self):
        self._nominal_BodyThrust = None  # type: unique symbol
        self.Force = None  # type: Vector3
        self.Location = None  # type: Vector3

class BodyVelocity:
    def __init__(self):
        self._nominal_BodyVelocity = None  # type: unique symbol
        self.MaxForce = None  # type: Vector3
        self.P = None  # type: float
        self.Velocity = None  # type: Vector3

class RocketPropulsion:
    def __init__(self):
        self._nominal_RocketPropulsion = None  # type: unique symbol
        self.CartoonFactor = None  # type: float
        self.MaxSpeed = None  # type: float
        self.MaxThrust = None  # type: float
        self.MaxTorque = None  # type: Vector3
        self.Target = None  # type: BasePart | undefined
        self.TargetOffset = None  # type: Vector3
        self.TargetRadius = None  # type: float
        self.ThrustD = None  # type: float
        self.ThrustP = None  # type: float
        self.TurnD = None  # type: float
        self.TurnP = None  # type: float
        self.ReachedTarget = None  # type: RBXScriptSignal<() => void>

class BodyPartDescription:
    def __init__(self):
        self._nominal_BodyPartDescription = None  # type: unique symbol
        self.AssetId = None  # type: float
        self.BodyPart = None  # type: Enum.BodyPart
        self.Color = None  # type: Color3
        self.Instance = None  # type: Instance | undefined

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
        self.CaptureBegan = None  # type: RBXScriptSignal<() => void>
        self.CaptureEnded = None  # type: RBXScriptSignal<() => void>
        self.CaptureSaved = None  # type: RBXScriptSignal<(captureInfo: Dict(str, unknown)) => void>
        self.UserCaptureSaved = None  # type: RBXScriptSignal<(captureContentId: ContentId) => void>

class CharacterAppearance:
    def __init__(self):
        self._nominal_CharacterAppearance = None  # type: unique symbol

class BodyColors:
    def __init__(self):
        self._nominal_BodyColors = None  # type: unique symbol
        self.HeadColor = None  # type: BrickColor
        self.HeadColor3 = None  # type: Color3
        self.LeftArmColor = None  # type: BrickColor
        self.LeftArmColor3 = None  # type: Color3
        self.LeftLegColor = None  # type: BrickColor
        self.LeftLegColor3 = None  # type: Color3
        self.RightArmColor = None  # type: BrickColor
        self.RightArmColor3 = None  # type: Color3
        self.RightLegColor = None  # type: BrickColor
        self.RightLegColor3 = None  # type: Color3
        self.TorsoColor = None  # type: BrickColor
        self.TorsoColor3 = None  # type: Color3

class CharacterMesh:
    def __init__(self):
        self._nominal_CharacterMesh = None  # type: unique symbol
        self.BaseTextureId = None  # type: float
        self.BodyPart = None  # type: Enum.BodyPart
        self.MeshId = None  # type: float
        self.OverlayTextureId = None  # type: float

class Clothing:
    def __init__(self):
        self._nominal_Clothing = None  # type: unique symbol
        self.Color3 = None  # type: Color3

class Pants:
    def __init__(self):
        self._nominal_Pants = None  # type: unique symbol
        self.PantsTemplate = None  # type: ContentId

class Shirt:
    def __init__(self):
        self._nominal_Shirt = None  # type: unique symbol
        self.ShirtTemplate = None  # type: ContentId

class ShirtGraphic:
    def __init__(self):
        self._nominal_ShirtGraphic = None  # type: unique symbol
        self.Color3 = None  # type: Color3
        self.Graphic = None  # type: ContentId

class Chat:
    def __init__(self):
        self._nominal_Chat = None  # type: unique symbol
        self.BubbleChatEnabled = None  # type: bool
        self.Chatted = None  # type: RBXScriptSignal<(part: BasePart, message: str, color: Enum.ChatColor) => void>

class ChatbotUIService:
    def __init__(self):
        self._nominal_ChatbotUIService = None  # type: unique symbol

class ClickDetector:
    def __init__(self):
        self._nominal_ClickDetector = None  # type: unique symbol
        self.CursorIcon = None  # type: ContentId
        self.MaxActivationDistance = None  # type: float
        self.MouseClick = None  # type: RBXScriptSignal<(playerWhoClicked: Player) => void>
        self.MouseHoverEnter = None  # type: RBXScriptSignal<(playerWhoHovered: Player) => void>
        self.MouseHoverLeave = None  # type: RBXScriptSignal<(playerWhoHovered: Player) => void>
        self.RightMouseClick = None  # type: RBXScriptSignal<(playerWhoClicked: Player) => void>

class DragDetector:
    def __init__(self):
        self._nominal_DragDetector = None  # type: unique symbol
        self.ActivatedCursorIcon = None  # type: ContentId
        self.ApplyAtCenterOfMass = None  # type: bool
        self.Axis = None  # type: Vector3
        self.DragFrame = None  # type: CFrame
        self.DragStyle = None  # type: Enum.DragDetectorDragStyle
        self.Enabled = None  # type: bool
        self.GamepadModeSwitchKeyCode = None  # type: Enum.KeyCode
        self.KeyboardModeSwitchKeyCode = None  # type: Enum.KeyCode
        self.MaxDragAngle = None  # type: float
        self.MaxDragTranslation = None  # type: Vector3
        self.MaxForce = None  # type: float
        self.MaxTorque = None  # type: float
        self.MinDragAngle = None  # type: float
        self.MinDragTranslation = None  # type: Vector3
        self.Orientation = None  # type: Vector3
        self.PermissionPolicy = None  # type: Enum.DragDetectorPermissionPolicy
        self.ReferenceInstance = None  # type: Instance | undefined
        self.ResponseStyle = None  # type: Enum.DragDetectorResponseStyle
        self.Responsiveness = None  # type: float
        self.RunLocally = None  # type: bool
        self.SecondaryAxis = None  # type: Vector3
        self.TrackballRadialPullFactor = None  # type: float
        self.TrackballRollFactor = None  # type: float
        self.VRSwitchKeyCode = None  # type: Enum.KeyCode
        self.WorldAxis = None  # type: Vector3
        self.WorldSecondaryAxis = None  # type: Vector3
        self.DragContinue = None  # type: RBXScriptSignal<(playerWhoDragged: Player, cursorRay: Ray, viewFrame: CFrame, vrInputFrame: CFrame | undefined, isModeSwitchKeyDown: bool) => void>
        self.DragContinueReplicate = None  # type: RBXScriptSignal<(playerWhoDragged: Player, cursorRay: Ray, viewFrame: CFrame, vrInputFrame: CFrame | undefined, isModeSwitchKeyDown: bool) => void>
        self.DragEnd = None  # type: RBXScriptSignal<(playerWhoDragged: Player) => void>
        self.DragEndReplicate = None  # type: RBXScriptSignal<(playerWhoDragged: Player) => void>
        self.DragStart = None  # type: RBXScriptSignal<(playerWhoDragged: Player, cursorRay: Ray, viewFrame: CFrame, hitFrame: CFrame, clickedPart: BasePart, vrInputFrame: CFrame | undefined, isModeSwitchKeyDown: bool) => void>
        self.DragStartReplicate = None  # type: RBXScriptSignal<(playerWhoDragged: Player, cursorRay: Ray, viewFrame: CFrame, hitFrame: CFrame, clickedPart: BasePart, vrInputFrame: CFrame | undefined, isModeSwitchKeyDown: bool) => void>
        self.RestartPhysicalDragReplicate = None  # type: RBXScriptSignal<(hitPoint: Vector3) => void>

class CloudCRUDService:
    def __init__(self):
        self._nominal_CloudCRUDService = None  # type: unique symbol

class Clouds:
    def __init__(self):
        self._nominal_Clouds = None  # type: unique symbol
        self.Color = None  # type: Color3
        self.Cover = None  # type: float
        self.Density = None  # type: float
        self.Enabled = None  # type: bool

class Collaborator:
    def __init__(self):
        self._nominal_Collaborator = None  # type: unique symbol
        self.CFrame = None  # type: CFrame
        self.CollaboratorColor = None  # type: float
        self.CollaboratorColor3 = None  # type: Color3
        self.CurDocGUID = None  # type: str
        self.CurScriptLineNumber = None  # type: float
        self.IsIdle = None  # type: bool
        self.Status = None  # type: Enum.CollaboratorStatus
        self.UserId = None  # type: float
        self.Username = None  # type: str

class CollaboratorsService:
    def __init__(self):
        self._nominal_CollaboratorsService = None  # type: unique symbol

class CollectionService:
    def __init__(self):
        self._nominal_CollectionService = None  # type: unique symbol
        self.ItemAdded = None  # type: RBXScriptSignal<(instance: Instance) => void>
        self.ItemRemoved = None  # type: RBXScriptSignal<(instance: Instance) => void>
        self.TagAdded = None  # type: RBXScriptSignal<(tag: str) => void>
        self.TagRemoved = None  # type: RBXScriptSignal<(tag: str) => void>

class CommandInstance:
    def __init__(self):
        self._nominal_CommandInstance = None  # type: unique symbol
        self.AllowGUIAccessPoints = None  # type: bool
        self.DisplayName = None  # type: str
        self.Name = None  # type: str

class CommandService:
    def __init__(self):
        self._nominal_CommandService = None  # type: unique symbol

class CommerceService:
    def __init__(self):
        self._nominal_CommerceService = None  # type: unique symbol
        self.PromptCommerceProductPurchaseFinished = None  # type: RBXScriptSignal<(user: Player, productId: str) => void>

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
        self.Active = None  # type: bool
        self.Attachment0 = None  # type: Attachment | undefined
        self.Attachment1 = None  # type: Attachment | undefined
        self.Color = None  # type: BrickColor
        self.Enabled = None  # type: bool
        self.Visible = None  # type: bool

class AlignOrientation:
    def __init__(self):
        self._nominal_AlignOrientation = None  # type: unique symbol
        self.AlignType = None  # type: Enum.AlignType
        self.CFrame = None  # type: CFrame
        self.LookAtPosition = None  # type: Vector3
        self.MaxAngularVelocity = None  # type: float
        self.MaxTorque = None  # type: float
        self.Mode = None  # type: Enum.OrientationAlignmentMode
        self.PrimaryAxis = None  # type: Vector3
        self.PrimaryAxisOnly = None  # type: bool
        self.ReactionTorqueEnabled = None  # type: bool
        self.Responsiveness = None  # type: float
        self.RigidityEnabled = None  # type: bool
        self.SecondaryAxis = None  # type: Vector3

class AlignPosition:
    def __init__(self):
        self._nominal_AlignPosition = None  # type: unique symbol
        self.ApplyAtCenterOfMass = None  # type: bool
        self.ForceLimitMode = None  # type: Enum.ForceLimitMode
        self.ForceRelativeTo = None  # type: Enum.ActuatorRelativeTo
        self.MaxAxesForce = None  # type: Vector3
        self.MaxForce = None  # type: float
        self.MaxVelocity = None  # type: float
        self.Mode = None  # type: Enum.PositionAlignmentMode
        self.Position = None  # type: Vector3
        self.ReactionForceEnabled = None  # type: bool
        self.Responsiveness = None  # type: float
        self.RigidityEnabled = None  # type: bool

class AngularVelocity:
    def __init__(self):
        self._nominal_AngularVelocity = None  # type: unique symbol
        self.AngularVelocity = None  # type: Vector3
        self.MaxTorque = None  # type: float
        self.ReactionTorqueEnabled = None  # type: bool
        self.RelativeTo = None  # type: Enum.ActuatorRelativeTo

class AnimationConstraint:
    def __init__(self):
        self._nominal_AnimationConstraint = None  # type: unique symbol
        self.C0 = None  # type: CFrame
        self.C1 = None  # type: CFrame
        self.IsKinematic = None  # type: bool
        self.MaxForce = None  # type: float
        self.MaxTorque = None  # type: float
        self.Part0 = None  # type: BasePart | undefined
        self.Part1 = None  # type: BasePart | undefined
        self.Transform = None  # type: CFrame

class BallSocketConstraint:
    def __init__(self):
        self._nominal_BallSocketConstraint = None  # type: unique symbol
        self.LimitsEnabled = None  # type: bool
        self.MaxFrictionTorque = None  # type: float
        self.Radius = None  # type: float
        self.Restitution = None  # type: float
        self.TwistLimitsEnabled = None  # type: bool
        self.TwistLowerAngle = None  # type: float
        self.TwistUpperAngle = None  # type: float
        self.UpperAngle = None  # type: float

class HingeConstraint:
    def __init__(self):
        self._nominal_HingeConstraint = None  # type: unique symbol
        self.ActuatorType = None  # type: Enum.ActuatorType
        self.AngularResponsiveness = None  # type: float
        self.AngularSpeed = None  # type: float
        self.AngularVelocity = None  # type: float
        self.CurrentAngle = None  # type: float
        self.LimitsEnabled = None  # type: bool
        self.LowerAngle = None  # type: float
        self.MotorMaxAcceleration = None  # type: float
        self.MotorMaxTorque = None  # type: float
        self.Radius = None  # type: float
        self.Restitution = None  # type: float
        self.ServoMaxTorque = None  # type: float
        self.SoftlockServoUponReachingTarget = None  # type: bool
        self.TargetAngle = None  # type: float
        self.UpperAngle = None  # type: float

class LineForce:
    def __init__(self):
        self._nominal_LineForce = None  # type: unique symbol
        self.ApplyAtCenterOfMass = None  # type: bool
        self.InverseSquareLaw = None  # type: bool
        self.Magnitude = None  # type: float
        self.MaxForce = None  # type: float
        self.ReactionForceEnabled = None  # type: bool

class LinearVelocity:
    def __init__(self):
        self._nominal_LinearVelocity = None  # type: unique symbol
        self.ForceLimitMode = None  # type: Enum.ForceLimitMode
        self.ForceLimitsEnabled = None  # type: bool
        self.LineDirection = None  # type: Vector3
        self.LineVelocity = None  # type: float
        self.MaxAxesForce = None  # type: Vector3
        self.MaxForce = None  # type: float
        self.MaxPlanarAxesForce = None  # type: Vector2
        self.PlaneVelocity = None  # type: Vector2
        self.PrimaryTangentAxis = None  # type: Vector3
        self.ReactionForceEnabled = None  # type: bool
        self.RelativeTo = None  # type: Enum.ActuatorRelativeTo
        self.SecondaryTangentAxis = None  # type: Vector3
        self.VectorVelocity = None  # type: Vector3
        self.VelocityConstraintMode = None  # type: Enum.VelocityConstraintMode

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
        self.CurrentDistance = None  # type: float
        self.Length = None  # type: float
        self.LimitAngle0 = None  # type: float
        self.LimitAngle1 = None  # type: float
        self.LimitsEnabled = None  # type: bool
        self.Thickness = None  # type: float

class RopeConstraint:
    def __init__(self):
        self._nominal_RopeConstraint = None  # type: unique symbol
        self.CurrentDistance = None  # type: float
        self.Length = None  # type: float
        self.Restitution = None  # type: float
        self.Thickness = None  # type: float
        self.WinchEnabled = None  # type: bool
        self.WinchForce = None  # type: float
        self.WinchResponsiveness = None  # type: float
        self.WinchSpeed = None  # type: float
        self.WinchTarget = None  # type: float

class SlidingBallConstraint:
    def __init__(self):
        self._nominal_SlidingBallConstraint = None  # type: unique symbol
        self.ActuatorType = None  # type: Enum.ActuatorType
        self.CurrentPosition = None  # type: float
        self.LimitsEnabled = None  # type: bool
        self.LinearResponsiveness = None  # type: float
        self.LowerLimit = None  # type: float
        self.MotorMaxAcceleration = None  # type: float
        self.MotorMaxForce = None  # type: float
        self.Restitution = None  # type: float
        self.ServoMaxForce = None  # type: float
        self.Size = None  # type: float
        self.SoftlockServoUponReachingTarget = None  # type: bool
        self.Speed = None  # type: float
        self.TargetPosition = None  # type: float
        self.UpperLimit = None  # type: float
        self.Velocity = None  # type: float

class CylindricalConstraint:
    def __init__(self):
        self._nominal_CylindricalConstraint = None  # type: unique symbol
        self.AngularActuatorType = None  # type: Enum.ActuatorType
        self.AngularLimitsEnabled = None  # type: bool
        self.AngularResponsiveness = None  # type: float
        self.AngularRestitution = None  # type: float
        self.AngularSpeed = None  # type: float
        self.AngularVelocity = None  # type: float
        self.CurrentAngle = None  # type: float
        self.InclinationAngle = None  # type: float
        self.LowerAngle = None  # type: float
        self.MotorMaxAngularAcceleration = None  # type: float
        self.MotorMaxTorque = None  # type: float
        self.RotationAxisVisible = None  # type: bool
        self.ServoMaxTorque = None  # type: float
        self.SoftlockAngularServoUponReachingTarget = None  # type: bool
        self.TargetAngle = None  # type: float
        self.UpperAngle = None  # type: float
        self.WorldRotationAxis = None  # type: Vector3

class PrismaticConstraint:
    def __init__(self):
        self._nominal_PrismaticConstraint = None  # type: unique symbol

class SpringConstraint:
    def __init__(self):
        self._nominal_SpringConstraint = None  # type: unique symbol
        self.Coils = None  # type: float
        self.CurrentLength = None  # type: float
        self.Damping = None  # type: float
        self.FreeLength = None  # type: float
        self.LimitsEnabled = None  # type: bool
        self.MaxForce = None  # type: float
        self.MaxLength = None  # type: float
        self.MinLength = None  # type: float
        self.Radius = None  # type: float
        self.Stiffness = None  # type: float
        self.Thickness = None  # type: float

class Torque:
    def __init__(self):
        self._nominal_Torque = None  # type: unique symbol
        self.RelativeTo = None  # type: Enum.ActuatorRelativeTo
        self.Torque = None  # type: Vector3

class TorsionSpringConstraint:
    def __init__(self):
        self._nominal_TorsionSpringConstraint = None  # type: unique symbol
        self.Coils = None  # type: float
        self.CurrentAngle = None  # type: float
        self.Damping = None  # type: float
        self.LimitEnabled = None  # type: bool
        self.LimitsEnabled = None  # type: bool
        self.MaxAngle = None  # type: float
        self.MaxTorque = None  # type: float
        self.Radius = None  # type: float
        self.Restitution = None  # type: float
        self.Stiffness = None  # type: float

class UniversalConstraint:
    def __init__(self):
        self._nominal_UniversalConstraint = None  # type: unique symbol
        self.LimitsEnabled = None  # type: bool
        self.MaxAngle = None  # type: float
        self.Radius = None  # type: float
        self.Restitution = None  # type: float

class VectorForce:
    def __init__(self):
        self._nominal_VectorForce = None  # type: unique symbol
        self.ApplyAtCenterOfMass = None  # type: bool
        self.Force = None  # type: Vector3
        self.RelativeTo = None  # type: Enum.ActuatorRelativeTo

class ContentProvider:
    def __init__(self):
        self._nominal_ContentProvider = None  # type: unique symbol
        self.BaseUrl = None  # type: str
        self.RequestQueueSize = None  # type: float
        self.AssetFetchFailed = None  # type: RBXScriptSignal<(assetId: ContentId) => void>

class ContextActionService:
    def __init__(self):
        self._nominal_ContextActionService = None  # type: unique symbol
        self.LocalToolEquipped = None  # type: RBXScriptSignal<(toolEquipped: Instance) => void>
        self.LocalToolUnequipped = None  # type: RBXScriptSignal<(toolUnequipped: Instance) => void>

class Controller:
    def __init__(self):
        self._nominal_Controller = None  # type: unique symbol
        self.ButtonChanged = None  # type: RBXScriptSignal<(button: Enum.Button) => void>

class HumanoidController:
    def __init__(self):
        self._nominal_HumanoidController = None  # type: unique symbol

class SkateboardController:
    def __init__(self):
        self._nominal_SkateboardController = None  # type: unique symbol
        self.Steer = None  # type: float
        self.Throttle = None  # type: float
        self.AxisChanged = None  # type: RBXScriptSignal<(axis: str) => void>

class VehicleController:
    def __init__(self):
        self._nominal_VehicleController = None  # type: unique symbol

class ControllerBase:
    def __init__(self):
        self._nominal_ControllerBase = None  # type: unique symbol
        self.Active = None  # type: bool
        self.BalanceRigidityEnabled = None  # type: bool
        self.MoveSpeedFactor = None  # type: float

class AirController:
    def __init__(self):
        self._nominal_AirController = None  # type: unique symbol
        self.BalanceMaxTorque = None  # type: float
        self.BalanceSpeed = None  # type: float
        self.LinearImpulse = None  # type: Vector3
        self.MaintainAngularMomentum = None  # type: bool
        self.MaintainLinearMomentum = None  # type: bool
        self.MoveMaxForce = None  # type: float
        self.TurnMaxTorque = None  # type: float
        self.TurnSpeedFactor = None  # type: float

class ClimbController:
    def __init__(self):
        self._nominal_ClimbController = None  # type: unique symbol
        self.AccelerationTime = None  # type: float
        self.BalanceMaxTorque = None  # type: float
        self.BalanceSpeed = None  # type: float
        self.MoveMaxForce = None  # type: float

class GroundController:
    def __init__(self):
        self._nominal_GroundController = None  # type: unique symbol
        self.AccelerationLean = None  # type: float
        self.AccelerationTime = None  # type: float
        self.BalanceMaxTorque = None  # type: float
        self.BalanceSpeed = None  # type: float
        self.DecelerationTime = None  # type: float
        self.Friction = None  # type: float
        self.FrictionWeight = None  # type: float
        self.GroundOffset = None  # type: float
        self.StandForce = None  # type: float
        self.StandSpeed = None  # type: float
        self.TurnSpeedFactor = None  # type: float

class SwimController:
    def __init__(self):
        self._nominal_SwimController = None  # type: unique symbol
        self.AccelerationTime = None  # type: float
        self.PitchMaxTorque = None  # type: float
        self.PitchSpeedFactor = None  # type: float
        self.RollMaxTorque = None  # type: float
        self.RollSpeedFactor = None  # type: float

class ControllerManager:
    def __init__(self):
        self._nominal_ControllerManager = None  # type: unique symbol
        self.ActiveController = None  # type: ControllerBase | undefined
        self.BaseMoveSpeed = None  # type: float
        self.BaseTurnSpeed = None  # type: float
        self.ClimbSensor = None  # type: ControllerSensor | undefined
        self.FacingDirection = None  # type: Vector3
        self.GroundSensor = None  # type: ControllerSensor | undefined
        self.MovingDirection = None  # type: Vector3
        self.RootPart = None  # type: BasePart | undefined
        self.UpDirection = None  # type: Vector3

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
        self.Offset = None  # type: Vector3
        self.Scale = None  # type: Vector3
        self.VertexColor = None  # type: Vector3

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
        self.MeshId = None  # type: ContentId
        self.TextureId = None  # type: ContentId

class SpecialMesh:
    def __init__(self):
        self._nominal_SpecialMesh = None  # type: unique symbol
        self.MeshType = None  # type: Enum.MeshType

class DataModelPatchService:
    def __init__(self):
        self._nominal_DataModelPatchService = None  # type: unique symbol

class DataStoreGetOptions:
    def __init__(self):
        self._nominal_DataStoreGetOptions = None  # type: unique symbol
        self.UseCache = None  # type: bool

class DataStoreIncrementOptions:
    def __init__(self):
        self._nominal_DataStoreIncrementOptions = None  # type: unique symbol

class DataStoreInfo:
    def __init__(self):
        self._nominal_DataStoreInfo = None  # type: unique symbol
        self.CreatedTime = None  # type: float
        self.DataStoreName = None  # type: str
        self.UpdatedTime = None  # type: float

class DataStoreKey:
    def __init__(self):
        self._nominal_DataStoreKey = None  # type: unique symbol
        self.KeyName = None  # type: str

class DataStoreKeyInfo:
    def __init__(self):
        self._nominal_DataStoreKeyInfo = None  # type: unique symbol
        self.CreatedTime = None  # type: float
        self.UpdatedTime = None  # type: float
        self.Version = None  # type: str

class DataStoreObjectVersionInfo:
    def __init__(self):
        self._nominal_DataStoreObjectVersionInfo = None  # type: unique symbol
        self.CreatedTime = None  # type: float
        self.IsDeleted = None  # type: bool
        self.Version = None  # type: str

class DataStoreOptions:
    def __init__(self):
        self._nominal_DataStoreOptions = None  # type: unique symbol
        self.AllScopes = None  # type: bool

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
        self.BehaviorType = None  # type: Enum.DialogBehaviorType
        self.ConversationDistance = None  # type: float
        self.GoodbyeChoiceActive = None  # type: bool
        self.GoodbyeDialog = None  # type: str
        self.InUse = None  # type: bool
        self.InitialPrompt = None  # type: str
        self.Purpose = None  # type: Enum.DialogPurpose
        self.Tone = None  # type: Enum.DialogTone
        self.TriggerDistance = None  # type: float
        self.TriggerOffset = None  # type: Vector3
        self.DialogChoiceSelected = None  # type: RBXScriptSignal<(player: Player, dialogChoice: Dialog) => void>

class DialogChoice:
    def __init__(self):
        self._nominal_DialogChoice = None  # type: unique symbol
        self.GoodbyeChoiceActive = None  # type: bool
        self.GoodbyeDialog = None  # type: str
        self.ResponseDialog = None  # type: str
        self.UserDialog = None  # type: str

class Dragger:
    def __init__(self):
        self._nominal_Dragger = None  # type: unique symbol

class DraggerService:
    def __init__(self):
        self._nominal_DraggerService = None  # type: unique symbol
        self.AlignDraggedObjects = None  # type: bool
        self.AngleSnapEnabled = None  # type: bool
        self.AngleSnapIncrement = None  # type: float
        self.AnimateHover = None  # type: bool
        self.CollisionsEnabled = None  # type: bool
        self.DraggerCoordinateSpace = None  # type: Enum.DraggerCoordinateSpace
        self.DraggerMovementMode = None  # type: Enum.DraggerMovementMode
        self.GeometrySnapColor = None  # type: Color3
        self.HoverAnimateFrequency = None  # type: float
        self.HoverThickness = None  # type: float
        self.JointsEnabled = None  # type: bool
        self.LinearSnapEnabled = None  # type: bool
        self.LinearSnapIncrement = None  # type: float
        self.ShowHover = None  # type: bool
        self.ShowPivotIndicator = None  # type: bool

class EditableService:
    def __init__(self):
        self._nominal_EditableService = None  # type: unique symbol

class EulerRotationCurve:
    def __init__(self):
        self._nominal_EulerRotationCurve = None  # type: unique symbol
        self.RotationOrder = None  # type: Enum.RotationOrder

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
        self.InviteMessageId = None  # type: str
        self.InviteUser = None  # type: float
        self.LaunchData = None  # type: str
        self.PromptMessage = None  # type: str

class ExperienceNotificationService:
    def __init__(self):
        self._nominal_ExperienceNotificationService = None  # type: unique symbol
        self.OptInPromptClosed = None  # type: RBXScriptSignal<() => void>

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
        self.BlastPressure = None  # type: float
        self.BlastRadius = None  # type: float
        self.DestroyJointRadiusPercent = None  # type: float
        self.ExplosionType = None  # type: Enum.ExplosionType
        self.LocalTransparencyModifier = None  # type: float
        self.Position = None  # type: Vector3
        self.TimeScale = None  # type: float
        self.Visible = None  # type: bool
        self.Hit = None  # type: RBXScriptSignal<(part: BasePart, distance: float) => void>

class FaceAnimatorService:
    def __init__(self):
        self._nominal_FaceAnimatorService = None  # type: unique symbol

class FaceControls:
    def __init__(self):
        self._nominal_FaceControls = None  # type: unique symbol

class FaceInstance:
    def __init__(self):
        self._nominal_FaceInstance = None  # type: unique symbol
        self.Face = None  # type: Enum.NormalId

class Decal:
    def __init__(self):
        self._nominal_Decal = None  # type: unique symbol
        self.Color3 = None  # type: Color3
        self.LocalTransparencyModifier = None  # type: float
        self.Shiny = None  # type: float
        self.Specular = None  # type: float
        self.Texture = None  # type: ContentId
        self.TextureContent = None  # type: Content
        self.Transparency = None  # type: float
        self.ZIndex = None  # type: float

class Texture:
    def __init__(self):
        self._nominal_Texture = None  # type: unique symbol
        self.OffsetStudsU = None  # type: float
        self.OffsetStudsV = None  # type: float
        self.StudsPerTileU = None  # type: float
        self.StudsPerTileV = None  # type: float

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
        self.FaceId = None  # type: Enum.NormalId
        self.InOut = None  # type: Enum.InOut
        self.LeftRight = None  # type: Enum.LeftRight
        self.TopBottom = None  # type: Enum.TopBottom

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
        self.Color = None  # type: Color3
        self.Enabled = None  # type: bool
        self.Heat = None  # type: float
        self.LocalTransparencyModifier = None  # type: float
        self.SecondaryColor = None  # type: Color3
        self.Size = None  # type: float
        self.TimeScale = None  # type: float

class FloatCurve:
    def __init__(self):
        self._nominal_FloatCurve = None  # type: unique symbol
        self.Length = None  # type: float

class Folder:
    def __init__(self):
        self._nominal_Folder = None  # type: unique symbol

class ForceField:
    def __init__(self):
        self._nominal_ForceField = None  # type: unique symbol
        self.Visible = None  # type: bool

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
        self.Font = None  # type: Font
        self.RichText = None  # type: bool
        self.Size = None  # type: float
        self.Text = None  # type: str
        self.Width = None  # type: float

class GlobalDataStore:
    def __init__(self):
        self._nominal_GlobalDataStore = None  # type: unique symbol
        self.GetAsync = None  # type: unknown
        self.IncrementAsync = None  # type: unknown
        self.RemoveAsync = None  # type: unknown
        self.SetAsync = None  # type: unknown
        self.UpdateAsync = None  # type: unknown

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
        self.AbsolutePosition = None  # type: Vector2
        self.AbsoluteRotation = None  # type: float
        self.AbsoluteSize = None  # type: Vector2
        self.AutoLocalize = None  # type: bool
        self.Localize = None  # type: bool
        self.RootLocalizationTable = None  # type: LocalizationTable | undefined
        self.SelectionBehaviorDown = None  # type: Enum.SelectionBehavior
        self.SelectionBehaviorLeft = None  # type: Enum.SelectionBehavior
        self.SelectionBehaviorRight = None  # type: Enum.SelectionBehavior
        self.SelectionBehaviorUp = None  # type: Enum.SelectionBehavior
        self.SelectionGroup = None  # type: bool
        self.SelectionChanged = None  # type: RBXScriptSignal<(amISelected: bool, previousSelection: GuiObject, newSelection: GuiObject) => void>

class GuiObject:
    def __init__(self):
        self._nominal_GuiObject = None  # type: unique symbol
        self.Active = None  # type: bool
        self.AnchorPoint = None  # type: Vector2
        self.AutomaticSize = None  # type: Enum.AutomaticSize
        self.BackgroundColor = None  # type: BrickColor
        self.BackgroundColor3 = None  # type: Color3
        self.BackgroundTransparency = None  # type: float
        self.BorderColor = None  # type: BrickColor
        self.BorderColor3 = None  # type: Color3
        self.BorderMode = None  # type: Enum.BorderMode
        self.BorderSizePixel = None  # type: float
        self.ClipsDescendants = None  # type: bool
        self.Draggable = None  # type: bool
        self.GuiState = None  # type: Enum.GuiState
        self.Interactable = None  # type: bool
        self.LayoutOrder = None  # type: float
        self.NextSelectionDown = None  # type: GuiObject | undefined
        self.NextSelectionLeft = None  # type: GuiObject | undefined
        self.NextSelectionRight = None  # type: GuiObject | undefined
        self.NextSelectionUp = None  # type: GuiObject | undefined
        self.Position = None  # type: UDim2
        self.Rotation = None  # type: float
        self.Selectable = None  # type: bool
        self.SelectionImageObject = None  # type: GuiObject | undefined
        self.SelectionOrder = None  # type: float
        self.Size = None  # type: UDim2
        self.SizeConstraint = None  # type: Enum.SizeConstraint
        self.Transparency = None  # type: float
        self.Visible = None  # type: bool
        self.ZIndex = None  # type: float
        self.DragBegin = None  # type: RBXScriptSignal<(initialPosition: UDim2) => void>
        self.DragStopped = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.InputBegan = None  # type: RBXScriptSignal<(input: InputObject) => void>
        self.InputChanged = None  # type: RBXScriptSignal<(input: InputObject) => void>
        self.InputEnded = None  # type: RBXScriptSignal<(input: InputObject) => void>
        self.MouseEnter = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.MouseLeave = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.MouseMoved = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.MouseWheelBackward = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.MouseWheelForward = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.SelectionGained = None  # type: RBXScriptSignal<() => void>
        self.SelectionLost = None  # type: RBXScriptSignal<() => void>
        self.TouchLongPress = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), state: Enum.UserInputState) => void>
        self.TouchPan = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), totalTranslation: Vector2, velocity: Vector2, state: Enum.UserInputState) => void>
        self.TouchPinch = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), scale: float, velocity: float, state: Enum.UserInputState) => void>
        self.TouchRotate = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), rotation: float, velocity: float, state: Enum.UserInputState) => void>
        self.TouchSwipe = None  # type: RBXScriptSignal<(swipeDirection: Enum.SwipeDirection, numberOfTouches: float) => void>
        self.TouchTap = None  # type: RBXScriptSignal<(touchPositions: List(Vector2)) => void>

class CanvasGroup:
    def __init__(self):
        self._nominal_CanvasGroup = None  # type: unique symbol
        self.GroupColor3 = None  # type: Color3
        self.GroupTransparency = None  # type: float

class Frame:
    def __init__(self):
        self._nominal_Frame = None  # type: unique symbol
        self.Style = None  # type: Enum.FrameStyle

class GuiButton:
    def __init__(self):
        self._nominal_GuiButton = None  # type: unique symbol
        self.AutoButtonColor = None  # type: bool
        self.HoverHapticEffect = None  # type: HapticEffect | undefined
        self.Modal = None  # type: bool
        self.PressHapticEffect = None  # type: HapticEffect | undefined
        self.Selected = None  # type: bool
        self.Style = None  # type: Enum.ButtonStyle
        self.Activated = None  # type: RBXScriptSignal<(inputObject: InputObject, clickCount: float) => void>
        self.MouseButton1Click = None  # type: RBXScriptSignal<() => void>
        self.MouseButton1Down = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.MouseButton1Up = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.MouseButton2Click = None  # type: RBXScriptSignal<() => void>
        self.MouseButton2Down = None  # type: RBXScriptSignal<(x: float, y: float) => void>
        self.MouseButton2Up = None  # type: RBXScriptSignal<(x: float, y: float) => void>

class ImageButton:
    def __init__(self):
        self._nominal_ImageButton = None  # type: unique symbol
        self.HoverImage = None  # type: ContentId
        self.HoverImageContent = None  # type: Content
        self.Image = None  # type: ContentId
        self.ImageColor3 = None  # type: Color3
        self.ImageContent = None  # type: Content
        self.ImageRectOffset = None  # type: Vector2
        self.ImageRectSize = None  # type: Vector2
        self.ImageTransparency = None  # type: float
        self.IsLoaded = None  # type: bool
        self.PressedImage = None  # type: ContentId
        self.PressedImageContent = None  # type: Content
        self.ResampleMode = None  # type: Enum.ResamplerMode
        self.ScaleType = None  # type: Enum.ScaleType
        self.SliceCenter = None  # type: Rect
        self.SliceScale = None  # type: float
        self.TileSize = None  # type: UDim2

class TextButton:
    def __init__(self):
        self._nominal_TextButton = None  # type: unique symbol
        self.ContentText = None  # type: str
        self.Font = None  # type: Enum.Font
        self.FontFace = None  # type: Font
        self.FontSize = None  # type: Enum.FontSize
        self.LineHeight = None  # type: float
        self.LocalizedText = None  # type: str
        self.MaxVisibleGraphemes = None  # type: float
        self.OpenTypeFeatures = None  # type: str
        self.OpenTypeFeaturesError = None  # type: str
        self.RichText = None  # type: bool
        self.Text = None  # type: str
        self.TextBounds = None  # type: Vector2
        self.TextColor = None  # type: BrickColor
        self.TextColor3 = None  # type: Color3
        self.TextDirection = None  # type: Enum.TextDirection
        self.TextFits = None  # type: bool
        self.TextScaled = None  # type: bool
        self.TextSize = None  # type: float
        self.TextStrokeColor3 = None  # type: Color3
        self.TextStrokeTransparency = None  # type: float
        self.TextTransparency = None  # type: float
        self.TextTruncate = None  # type: Enum.TextTruncate
        self.TextWrap = None  # type: bool
        self.TextWrapped = None  # type: bool
        self.TextXAlignment = None  # type: Enum.TextXAlignment
        self.TextYAlignment = None  # type: Enum.TextYAlignment

class GuiLabel:
    def __init__(self):
        self._nominal_GuiLabel = None  # type: unique symbol

class ImageLabel:
    def __init__(self):
        self._nominal_ImageLabel = None  # type: unique symbol
        self.Image = None  # type: ContentId
        self.ImageColor3 = None  # type: Color3
        self.ImageContent = None  # type: Content
        self.ImageRectOffset = None  # type: Vector2
        self.ImageRectSize = None  # type: Vector2
        self.ImageTransparency = None  # type: float
        self.IsLoaded = None  # type: bool
        self.ResampleMode = None  # type: Enum.ResamplerMode
        self.ScaleType = None  # type: Enum.ScaleType
        self.SliceCenter = None  # type: Rect
        self.SliceScale = None  # type: float
        self.TileSize = None  # type: UDim2

class TextLabel:
    def __init__(self):
        self._nominal_TextLabel = None  # type: unique symbol
        self.ContentText = None  # type: str
        self.Font = None  # type: Enum.Font
        self.FontFace = None  # type: Font
        self.FontSize = None  # type: Enum.FontSize
        self.LineHeight = None  # type: float
        self.LocalizedText = None  # type: str
        self.MaxVisibleGraphemes = None  # type: float
        self.OpenTypeFeatures = None  # type: str
        self.OpenTypeFeaturesError = None  # type: str
        self.RichText = None  # type: bool
        self.Text = None  # type: str
        self.TextBounds = None  # type: Vector2
        self.TextColor = None  # type: BrickColor
        self.TextColor3 = None  # type: Color3
        self.TextDirection = None  # type: Enum.TextDirection
        self.TextFits = None  # type: bool
        self.TextScaled = None  # type: bool
        self.TextSize = None  # type: float
        self.TextStrokeColor3 = None  # type: Color3
        self.TextStrokeTransparency = None  # type: float
        self.TextTransparency = None  # type: float
        self.TextTruncate = None  # type: Enum.TextTruncate
        self.TextWrap = None  # type: bool
        self.TextWrapped = None  # type: bool
        self.TextXAlignment = None  # type: Enum.TextXAlignment
        self.TextYAlignment = None  # type: Enum.TextYAlignment

class RelativeGui:
    def __init__(self):
        self._nominal_RelativeGui = None  # type: unique symbol

class ScrollingFrame:
    def __init__(self):
        self._nominal_ScrollingFrame = None  # type: unique symbol
        self.AbsoluteCanvasSize = None  # type: Vector2
        self.AbsoluteWindowSize = None  # type: Vector2
        self.AutomaticCanvasSize = None  # type: Enum.AutomaticSize
        self.BottomImage = None  # type: ContentId
        self.CanvasPosition = None  # type: Vector2
        self.CanvasSize = None  # type: UDim2
        self.ElasticBehavior = None  # type: Enum.ElasticBehavior
        self.HorizontalScrollBarInset = None  # type: Enum.ScrollBarInset
        self.MidImage = None  # type: ContentId
        self.ScrollBarImageColor3 = None  # type: Color3
        self.ScrollBarImageTransparency = None  # type: float
        self.ScrollBarThickness = None  # type: float
        self.ScrollingDirection = None  # type: Enum.ScrollingDirection
        self.ScrollingEnabled = None  # type: bool
        self.TopImage = None  # type: ContentId
        self.VerticalScrollBarInset = None  # type: Enum.ScrollBarInset
        self.VerticalScrollBarPosition = None  # type: Enum.VerticalScrollBarPosition

class TextBox:
    def __init__(self):
        self._nominal_TextBox = None  # type: unique symbol
        self.ClearTextOnFocus = None  # type: bool
        self.ContentText = None  # type: str
        self.CursorPosition = None  # type: float
        self.Font = None  # type: Enum.Font
        self.FontFace = None  # type: Font
        self.FontSize = None  # type: Enum.FontSize
        self.LineHeight = None  # type: float
        self.MaxVisibleGraphemes = None  # type: float
        self.MultiLine = None  # type: bool
        self.OpenTypeFeatures = None  # type: str
        self.OpenTypeFeaturesError = None  # type: str
        self.PlaceholderColor3 = None  # type: Color3
        self.PlaceholderText = None  # type: str
        self.RichText = None  # type: bool
        self.SelectionStart = None  # type: float
        self.ShowNativeInput = None  # type: bool
        self.Text = None  # type: str
        self.TextBounds = None  # type: Vector2
        self.TextColor = None  # type: BrickColor
        self.TextColor3 = None  # type: Color3
        self.TextDirection = None  # type: Enum.TextDirection
        self.TextEditable = None  # type: bool
        self.TextFits = None  # type: bool
        self.TextScaled = None  # type: bool
        self.TextSize = None  # type: float
        self.TextStrokeColor3 = None  # type: Color3
        self.TextStrokeTransparency = None  # type: float
        self.TextTransparency = None  # type: float
        self.TextTruncate = None  # type: Enum.TextTruncate
        self.TextWrap = None  # type: bool
        self.TextWrapped = None  # type: bool
        self.TextXAlignment = None  # type: Enum.TextXAlignment
        self.TextYAlignment = None  # type: Enum.TextYAlignment
        self.FocusLost = None  # type: RBXScriptSignal<(enterPressed: bool, inputThatCausedFocusLoss: InputObject) => void>
        self.Focused = None  # type: RBXScriptSignal<() => void>
        self.ReturnPressedFromOnScreenKeyboard = None  # type: RBXScriptSignal<() => void>

class VideoDisplay:
    def __init__(self):
        self._nominal_VideoDisplay = None  # type: unique symbol
        self.ResampleMode = None  # type: Enum.ResamplerMode
        self.ScaleType = None  # type: Enum.ScaleType
        self.TileSize = None  # type: UDim2
        self.VideoColor3 = None  # type: Color3
        self.VideoRectOffset = None  # type: Vector2
        self.VideoRectSize = None  # type: Vector2
        self.VideoTransparency = None  # type: float
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

class VideoFrame:
    def __init__(self):
        self._nominal_VideoFrame = None  # type: unique symbol
        self.IsLoaded = None  # type: bool
        self.Looped = None  # type: bool
        self.Playing = None  # type: bool
        self.Resolution = None  # type: Vector2
        self.TimeLength = None  # type: float
        self.TimePosition = None  # type: float
        self.Video = None  # type: ContentId
        self.Volume = None  # type: float
        self.DidLoop = None  # type: RBXScriptSignal<(video: str) => void>
        self.Ended = None  # type: RBXScriptSignal<(video: str) => void>
        self.Loaded = None  # type: RBXScriptSignal<(video: str) => void>
        self.Paused = None  # type: RBXScriptSignal<(video: str) => void>
        self.Played = None  # type: RBXScriptSignal<(video: str) => void>

class ViewportFrame:
    def __init__(self):
        self._nominal_ViewportFrame = None  # type: unique symbol
        self.Ambient = None  # type: Color3
        self.CurrentCamera = None  # type: Camera | undefined
        self.ImageColor3 = None  # type: Color3
        self.ImageTransparency = None  # type: float
        self.LightColor = None  # type: Color3
        self.LightDirection = None  # type: Vector3

class LayerCollector:
    def __init__(self):
        self._nominal_LayerCollector = None  # type: unique symbol
        self.Enabled = None  # type: bool
        self.ResetOnSpawn = None  # type: bool
        self.ZIndexBehavior = None  # type: Enum.ZIndexBehavior

class BillboardGui:
    def __init__(self):
        self._nominal_BillboardGui = None  # type: unique symbol
        self.Active = None  # type: bool
        self.Adornee = None  # type: PVInstance | Attachment | undefined
        self.AlwaysOnTop = None  # type: bool
        self.Brightness = None  # type: float
        self.ClipsDescendants = None  # type: bool
        self.CurrentDistance = None  # type: float
        self.DistanceLowerLimit = None  # type: float
        self.DistanceStep = None  # type: float
        self.DistanceUpperLimit = None  # type: float
        self.ExtentsOffset = None  # type: Vector3
        self.ExtentsOffsetWorldSpace = None  # type: Vector3
        self.LightInfluence = None  # type: float
        self.MaxDistance = None  # type: float
        self.PlayerToHideFrom = None  # type: Player | undefined
        self.Size = None  # type: UDim2
        self.SizeOffset = None  # type: Vector2
        self.StudsOffset = None  # type: Vector3
        self.StudsOffsetWorldSpace = None  # type: Vector3

class ScreenGui:
    def __init__(self):
        self._nominal_ScreenGui = None  # type: unique symbol
        self.ClipToDeviceSafeArea = None  # type: bool
        self.DisplayOrder = None  # type: float
        self.IgnoreGuiInset = None  # type: bool
        self.SafeAreaCompatibility = None  # type: Enum.SafeAreaCompatibility
        self.ScreenInsets = None  # type: Enum.ScreenInsets

class SurfaceGuiBase:
    def __init__(self):
        self._nominal_SurfaceGuiBase = None  # type: unique symbol
        self.Active = None  # type: bool
        self.Adornee = None  # type: BasePart | undefined
        self.Face = None  # type: Enum.NormalId

class AdGui:
    def __init__(self):
        self._nominal_AdGui = None  # type: unique symbol
        self.AdShape = None  # type: Enum.AdShape
        self.EnableVideoAds = None  # type: bool
        self.FallbackImage = None  # type: ContentId
        self.Status = None  # type: Enum.AdUnitStatus
        self.OnAdEvent = None  # type: ((eventInfo: object) => bool) | undefined

class SurfaceGui:
    def __init__(self):
        self._nominal_SurfaceGui = None  # type: unique symbol
        self.AlwaysOnTop = None  # type: bool
        self.Brightness = None  # type: float
        self.CanvasSize = None  # type: Vector2
        self.ClipsDescendants = None  # type: bool
        self.LightInfluence = None  # type: float
        self.MaxDistance = None  # type: float
        self.PixelsPerStud = None  # type: float
        self.SizingMode = None  # type: Enum.SurfaceGuiSizingMode
        self.ToolPunchThroughDistance = None  # type: float
        self.ZOffset = None  # type: float

class GuiBase3d:
    def __init__(self):
        self._nominal_GuiBase3d = None  # type: unique symbol
        self.Color3 = None  # type: Color3
        self.Transparency = None  # type: float
        self.Visible = None  # type: bool

class FloorWire:
    def __init__(self):
        self._nominal_FloorWire = None  # type: unique symbol
        self.CycleOffset = None  # type: float
        self.From = None  # type: BasePart | undefined
        self.StudsBetweenTextures = None  # type: float
        self.Texture = None  # type: ContentId
        self.TextureSize = None  # type: Vector2
        self.To = None  # type: BasePart | undefined
        self.Velocity = None  # type: float
        self.WireRadius = None  # type: float

class InstanceAdornment:
    def __init__(self):
        self._nominal_InstanceAdornment = None  # type: unique symbol
        self.Adornee = None  # type: Instance | undefined

class SelectionBox:
    def __init__(self):
        self._nominal_SelectionBox = None  # type: unique symbol
        self.LineThickness = None  # type: float
        self.SurfaceColor = None  # type: BrickColor
        self.SurfaceColor3 = None  # type: Color3
        self.SurfaceTransparency = None  # type: float

class PVAdornment:
    def __init__(self):
        self._nominal_PVAdornment = None  # type: unique symbol
        self.Adornee = None  # type: PVInstance | undefined

class HandleAdornment:
    def __init__(self):
        self._nominal_HandleAdornment = None  # type: unique symbol
        self.AdornCullingMode = None  # type: Enum.AdornCullingMode
        self.AlwaysOnTop = None  # type: bool
        self.CFrame = None  # type: CFrame
        self.SizeRelativeOffset = None  # type: Vector3
        self.ZIndex = None  # type: float
        self.MouseButton1Down = None  # type: RBXScriptSignal<() => void>
        self.MouseButton1Up = None  # type: RBXScriptSignal<() => void>
        self.MouseEnter = None  # type: RBXScriptSignal<() => void>
        self.MouseLeave = None  # type: RBXScriptSignal<() => void>

class BoxHandleAdornment:
    def __init__(self):
        self._nominal_BoxHandleAdornment = None  # type: unique symbol
        self.Size = None  # type: Vector3

class ConeHandleAdornment:
    def __init__(self):
        self._nominal_ConeHandleAdornment = None  # type: unique symbol
        self.Height = None  # type: float
        self.Radius = None  # type: float

class CylinderHandleAdornment:
    def __init__(self):
        self._nominal_CylinderHandleAdornment = None  # type: unique symbol
        self.Angle = None  # type: float
        self.Height = None  # type: float
        self.InnerRadius = None  # type: float
        self.Radius = None  # type: float

class ImageHandleAdornment:
    def __init__(self):
        self._nominal_ImageHandleAdornment = None  # type: unique symbol
        self.Image = None  # type: ContentId
        self.Size = None  # type: Vector2

class LineHandleAdornment:
    def __init__(self):
        self._nominal_LineHandleAdornment = None  # type: unique symbol
        self.Length = None  # type: float
        self.Thickness = None  # type: float

class SphereHandleAdornment:
    def __init__(self):
        self._nominal_SphereHandleAdornment = None  # type: unique symbol
        self.Radius = None  # type: float

class WireframeHandleAdornment:
    def __init__(self):
        self._nominal_WireframeHandleAdornment = None  # type: unique symbol
        self.Scale = None  # type: Vector3
        self.Thickness = None  # type: float

class ParabolaAdornment:
    def __init__(self):
        self._nominal_ParabolaAdornment = None  # type: unique symbol

class SelectionSphere:
    def __init__(self):
        self._nominal_SelectionSphere = None  # type: unique symbol
        self.SurfaceColor = None  # type: BrickColor
        self.SurfaceColor3 = None  # type: Color3
        self.SurfaceTransparency = None  # type: float

class PartAdornment:
    def __init__(self):
        self._nominal_PartAdornment = None  # type: unique symbol
        self.Adornee = None  # type: BasePart | undefined

class HandlesBase:
    def __init__(self):
        self._nominal_HandlesBase = None  # type: unique symbol

class ArcHandles:
    def __init__(self):
        self._nominal_ArcHandles = None  # type: unique symbol
        self.Axes = None  # type: Axes
        self.MouseButton1Down = None  # type: RBXScriptSignal<(axis: Enum.Axis) => void>
        self.MouseButton1Up = None  # type: RBXScriptSignal<(axis: Enum.Axis) => void>
        self.MouseDrag = None  # type: RBXScriptSignal<(axis: Enum.Axis, relativeAngle: float, deltaRadius: float) => void>
        self.MouseEnter = None  # type: RBXScriptSignal<(axis: Enum.Axis) => void>
        self.MouseLeave = None  # type: RBXScriptSignal<(axis: Enum.Axis) => void>

class Handles:
    def __init__(self):
        self._nominal_Handles = None  # type: unique symbol
        self.Faces = None  # type: Faces
        self.Style = None  # type: Enum.HandlesStyle
        self.MouseButton1Down = None  # type: RBXScriptSignal<(face: Enum.NormalId) => void>
        self.MouseButton1Up = None  # type: RBXScriptSignal<(face: Enum.NormalId) => void>
        self.MouseDrag = None  # type: RBXScriptSignal<(face: Enum.NormalId, distance: float) => void>
        self.MouseEnter = None  # type: RBXScriptSignal<(face: Enum.NormalId) => void>
        self.MouseLeave = None  # type: RBXScriptSignal<(face: Enum.NormalId) => void>

class SurfaceSelection:
    def __init__(self):
        self._nominal_SurfaceSelection = None  # type: unique symbol
        self.TargetSurface = None  # type: Enum.NormalId

class SelectionLasso:
    def __init__(self):
        self._nominal_SelectionLasso = None  # type: unique symbol
        self.Humanoid = None  # type: Humanoid | undefined

class SelectionPartLasso:
    def __init__(self):
        self._nominal_SelectionPartLasso = None  # type: unique symbol
        self.Part = None  # type: BasePart | undefined

class SelectionPointLasso:
    def __init__(self):
        self._nominal_SelectionPointLasso = None  # type: unique symbol
        self.Point = None  # type: Vector3

class Path2D:
    def __init__(self):
        self._nominal_Path2D = None  # type: unique symbol
        self.Closed = None  # type: bool
        self.Color3 = None  # type: Color3
        self.Thickness = None  # type: float
        self.Visible = None  # type: bool
        self.ZIndex = None  # type: float
        self.ControlPointChanged = None  # type: RBXScriptSignal<() => void>

class GuiService:
    def __init__(self):
        self._nominal_GuiService = None  # type: unique symbol
        self.AutoSelectGuiEnabled = None  # type: bool
        self.CoreGuiNavigationEnabled = None  # type: bool
        self.GuiNavigationEnabled = None  # type: bool
        self.IsModalDialog = None  # type: bool
        self.IsWindows = None  # type: bool
        self.MenuIsOpen = None  # type: bool
        self.PreferredTextSize = None  # type: Enum.PreferredTextSize
        self.PreferredTransparency = None  # type: float
        self.ReducedMotionEnabled = None  # type: bool
        self.SelectedObject = None  # type: GuiObject | undefined
        self.TopbarInset = None  # type: Rect
        self.TouchControlsEnabled = None  # type: bool
        self.MenuClosed = None  # type: RBXScriptSignal<() => void>
        self.MenuOpened = None  # type: RBXScriptSignal<() => void>

class HandRigDescription:
    def __init__(self):
        self._nominal_HandRigDescription = None  # type: unique symbol
        self.Index1 = None  # type: Instance | undefined
        self.Index1TposeAdjustment = None  # type: CFrame
        self.Index2 = None  # type: Instance | undefined
        self.Index2TposeAdjustment = None  # type: CFrame
        self.Index3 = None  # type: Instance | undefined
        self.Index3TposeAdjustment = None  # type: CFrame
        self.IndexRange = None  # type: Vector3
        self.IndexSize = None  # type: float
        self.Middle1 = None  # type: Instance | undefined
        self.Middle1TposeAdjustment = None  # type: CFrame
        self.Middle2 = None  # type: Instance | undefined
        self.Middle2TposeAdjustment = None  # type: CFrame
        self.Middle3 = None  # type: Instance | undefined
        self.Middle3TposeAdjustment = None  # type: CFrame
        self.MiddleRange = None  # type: Vector3
        self.MiddleSize = None  # type: float
        self.Pinky1 = None  # type: Instance | undefined
        self.Pinky1TposeAdjustment = None  # type: CFrame
        self.Pinky2 = None  # type: Instance | undefined
        self.Pinky2TposeAdjustment = None  # type: CFrame
        self.Pinky3 = None  # type: Instance | undefined
        self.Pinky3TposeAdjustment = None  # type: CFrame
        self.PinkyRange = None  # type: Vector3
        self.PinkySize = None  # type: float
        self.Ring1 = None  # type: Instance | undefined
        self.Ring1TposeAdjustment = None  # type: CFrame
        self.Ring2 = None  # type: Instance | undefined
        self.Ring2TposeAdjustment = None  # type: CFrame
        self.Ring3 = None  # type: Instance | undefined
        self.Ring3TposeAdjustment = None  # type: CFrame
        self.RingRange = None  # type: Vector3
        self.RingSize = None  # type: float
        self.Side = None  # type: Enum.HandRigDescriptionSide
        self.Thumb1 = None  # type: Instance | undefined
        self.Thumb1TposeAdjustment = None  # type: CFrame
        self.Thumb2 = None  # type: Instance | undefined
        self.Thumb2TposeAdjustment = None  # type: CFrame
        self.Thumb3 = None  # type: Instance | undefined
        self.Thumb3TposeAdjustment = None  # type: CFrame
        self.ThumbRange = None  # type: Vector3
        self.ThumbSize = None  # type: float

class HapticEffect:
    def __init__(self):
        self._nominal_HapticEffect = None  # type: unique symbol
        self.Looped = None  # type: bool
        self.Position = None  # type: Vector3
        self.Radius = None  # type: float
        self.Type = None  # type: Enum.HapticEffectType

class HapticService:
    def __init__(self):
        self._nominal_HapticService = None  # type: unique symbol

class HeapProfilerService:
    def __init__(self):
        self._nominal_HeapProfilerService = None  # type: unique symbol

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
        self.Adornee = None  # type: Instance | undefined
        self.DepthMode = None  # type: Enum.HighlightDepthMode
        self.Enabled = None  # type: bool
        self.FillColor = None  # type: Color3
        self.FillTransparency = None  # type: float
        self.OutlineColor = None  # type: Color3
        self.OutlineTransparency = None  # type: float

class HttpService:
    def __init__(self):
        self._nominal_HttpService = None  # type: unique symbol

class Humanoid:
    def __init__(self):
        self._nominal_Humanoid = None  # type: unique symbol
        self.AutoJumpEnabled = None  # type: bool
        self.AutoRotate = None  # type: bool
        self.AutomaticScalingEnabled = None  # type: bool
        self.BreakJointsOnDeath = None  # type: bool
        self.CameraOffset = None  # type: Vector3
        self.DisplayDistanceType = None  # type: Enum.HumanoidDisplayDistanceType
        self.DisplayName = None  # type: str
        self.EvaluateStateMachine = None  # type: bool
        self.FloorMaterial = None  # type: Enum.Material
        self.Health = None  # type: float
        self.HealthDisplayDistance = None  # type: float
        self.HealthDisplayType = None  # type: Enum.HumanoidHealthDisplayType
        self.HipHeight = None  # type: float
        self.Jump = None  # type: bool
        self.JumpHeight = None  # type: float
        self.JumpPower = None  # type: float
        self.LeftLeg = None  # type: BasePart | undefined
        self.MaxHealth = None  # type: float
        self.MaxSlopeAngle = None  # type: float
        self.MoveDirection = None  # type: Vector3
        self.NameDisplayDistance = None  # type: float
        self.NameOcclusion = None  # type: Enum.NameOcclusion
        self.PlatformStand = None  # type: bool
        self.RequiresNeck = None  # type: bool
        self.RigType = None  # type: Enum.HumanoidRigType
        self.RightLeg = None  # type: BasePart | undefined
        self.RootPart = None  # type: BasePart | undefined
        self.SeatPart = None  # type: BasePart | undefined
        self.Sit = None  # type: bool
        self.TargetPoint = None  # type: Vector3
        self.Torso = None  # type: BasePart | undefined
        self.UseJumpPower = None  # type: bool
        self.WalkSpeed = None  # type: float
        self.WalkToPart = None  # type: BasePart | undefined
        self.WalkToPoint = None  # type: Vector3
        self.AnimationPlayed = None  # type: RBXScriptSignal<(animationTrack: AnimationTrack) => void>
        self.ApplyDescriptionFinished = None  # type: RBXScriptSignal<(description: HumanoidDescription) => void>
        self.Climbing = None  # type: RBXScriptSignal<(speed: float) => void>
        self.CustomStatusAdded = None  # type: RBXScriptSignal<(status: str) => void>
        self.CustomStatusRemoved = None  # type: RBXScriptSignal<(status: str) => void>
        self.Died = None  # type: RBXScriptSignal<() => void>
        self.FallingDown = None  # type: RBXScriptSignal<(active: bool) => void>
        self.FreeFalling = None  # type: RBXScriptSignal<(active: bool) => void>
        self.GettingUp = None  # type: RBXScriptSignal<(active: bool) => void>
        self.HealthChanged = None  # type: RBXScriptSignal<(health: float) => void>
        self.Jumping = None  # type: RBXScriptSignal<(active: bool) => void>
        self.MoveToFinished = None  # type: RBXScriptSignal<(reached: bool) => void>
        self.PlatformStanding = None  # type: RBXScriptSignal<(active: bool) => void>
        self.Ragdoll = None  # type: RBXScriptSignal<(active: bool) => void>
        self.Running = None  # type: RBXScriptSignal<(speed: float) => void>
        self.Seated = None  # type: RBXScriptSignal<(active: bool, currentSeatPart: Seat | VehicleSeat | undefined) => void>
        self.StateChanged = None  # type: RBXScriptSignal<(oldValue: Enum.HumanoidStateType, newValue: Enum.HumanoidStateType) => void>
        self.StateEnabledChanged = None  # type: RBXScriptSignal<(state: Enum.HumanoidStateType, isEnabled: bool) => void>
        self.StatusAdded = None  # type: RBXScriptSignal<(status: Enum.Status) => void>
        self.StatusRemoved = None  # type: RBXScriptSignal<(status: Enum.Status) => void>
        self.Strafing = None  # type: RBXScriptSignal<(active: bool) => void>
        self.Swimming = None  # type: RBXScriptSignal<(speed: float) => void>
        self.Touched = None  # type: RBXScriptSignal<(touchingPart: BasePart, humanoidPart: BasePart) => void>

class HumanoidDescription:
    def __init__(self):
        self._nominal_HumanoidDescription = None  # type: unique symbol
        self.BackAccessory = None  # type: str
        self.BodyTypeScale = None  # type: float
        self.ClimbAnimation = None  # type: float
        self.DepthScale = None  # type: float
        self.Face = None  # type: float
        self.FaceAccessory = None  # type: str
        self.FallAnimation = None  # type: float
        self.FrontAccessory = None  # type: str
        self.GraphicTShirt = None  # type: float
        self.HairAccessory = None  # type: str
        self.HatAccessory = None  # type: str
        self.Head = None  # type: float
        self.HeadColor = None  # type: Color3
        self.HeadScale = None  # type: float
        self.HeightScale = None  # type: float
        self.IdleAnimation = None  # type: float
        self.JumpAnimation = None  # type: float
        self.LeftArm = None  # type: float
        self.LeftArmColor = None  # type: Color3
        self.LeftLeg = None  # type: float
        self.LeftLegColor = None  # type: Color3
        self.MoodAnimation = None  # type: float
        self.NeckAccessory = None  # type: str
        self.Pants = None  # type: float
        self.ProportionScale = None  # type: float
        self.RightArm = None  # type: float
        self.RightArmColor = None  # type: Color3
        self.RightLeg = None  # type: float
        self.RightLegColor = None  # type: Color3
        self.RunAnimation = None  # type: float
        self.Shirt = None  # type: float
        self.ShouldersAccessory = None  # type: str
        self.SwimAnimation = None  # type: float
        self.Torso = None  # type: float
        self.TorsoColor = None  # type: Color3
        self.WaistAccessory = None  # type: str
        self.WalkAnimation = None  # type: float
        self.WidthScale = None  # type: float
        self.EmotesChanged = None  # type: RBXScriptSignal<(newEmotes: EmoteDictionary) => void>
        self.EquippedEmotesChanged = None  # type: RBXScriptSignal<(newEquippedEmotes: EquippedEmotes) => void>

class HumanoidRigDescription:
    def __init__(self):
        self._nominal_HumanoidRigDescription = None  # type: unique symbol
        self.Chest = None  # type: Instance | undefined
        self.ChestRangeMax = None  # type: Vector3
        self.ChestRangeMin = None  # type: Vector3
        self.ChestSize = None  # type: float
        self.ChestTposeAdjustment = None  # type: CFrame
        self.Head = None  # type: Instance | undefined
        self.HeadRangeMax = None  # type: Vector3
        self.HeadRangeMin = None  # type: Vector3
        self.HeadSize = None  # type: float
        self.HeadTposeAdjustment = None  # type: CFrame
        self.LeftAnkle = None  # type: Instance | undefined
        self.LeftAnkleRangeMax = None  # type: Vector3
        self.LeftAnkleRangeMin = None  # type: Vector3
        self.LeftAnkleSize = None  # type: float
        self.LeftAnkleTposeAdjustment = None  # type: CFrame
        self.LeftClavicle = None  # type: Instance | undefined
        self.LeftClavicleRangeMax = None  # type: Vector3
        self.LeftClavicleRangeMin = None  # type: Vector3
        self.LeftClavicleSize = None  # type: float
        self.LeftClavicleTposeAdjustment = None  # type: CFrame
        self.LeftElbow = None  # type: Instance | undefined
        self.LeftElbowRangeMax = None  # type: Vector3
        self.LeftElbowRangeMin = None  # type: Vector3
        self.LeftElbowSize = None  # type: float
        self.LeftElbowTposeAdjustment = None  # type: CFrame
        self.LeftHip = None  # type: Instance | undefined
        self.LeftHipRangeMax = None  # type: Vector3
        self.LeftHipRangeMin = None  # type: Vector3
        self.LeftHipSize = None  # type: float
        self.LeftHipTposeAdjustment = None  # type: CFrame
        self.LeftKnee = None  # type: Instance | undefined
        self.LeftKneeRangeMax = None  # type: Vector3
        self.LeftKneeRangeMin = None  # type: Vector3
        self.LeftKneeSize = None  # type: float
        self.LeftKneeTposeAdjustment = None  # type: CFrame
        self.LeftShoulder = None  # type: Instance | undefined
        self.LeftShoulderRangeMax = None  # type: Vector3
        self.LeftShoulderRangeMin = None  # type: Vector3
        self.LeftShoulderSize = None  # type: float
        self.LeftShoulderTposeAdjustment = None  # type: CFrame
        self.LeftToes = None  # type: Instance | undefined
        self.LeftToesRangeMax = None  # type: Vector3
        self.LeftToesRangeMin = None  # type: Vector3
        self.LeftToesSize = None  # type: float
        self.LeftToesTposeAdjustment = None  # type: CFrame
        self.LeftWrist = None  # type: Instance | undefined
        self.LeftWristRangeMax = None  # type: Vector3
        self.LeftWristRangeMin = None  # type: Vector3
        self.LeftWristSize = None  # type: float
        self.LeftWristTposeAdjustment = None  # type: CFrame
        self.Neck = None  # type: Instance | undefined
        self.NeckRangeMax = None  # type: Vector3
        self.NeckRangeMin = None  # type: Vector3
        self.NeckSize = None  # type: float
        self.NeckTposeAdjustment = None  # type: CFrame
        self.Pelvis = None  # type: Instance | undefined
        self.PelvisRangeMax = None  # type: Vector3
        self.PelvisRangeMin = None  # type: Vector3
        self.PelvisSize = None  # type: float
        self.PelvisTposeAdjustment = None  # type: CFrame
        self.RightAnkle = None  # type: Instance | undefined
        self.RightAnkleRangeMax = None  # type: Vector3
        self.RightAnkleRangeMin = None  # type: Vector3
        self.RightAnkleSize = None  # type: float
        self.RightAnkleTposeAdjustment = None  # type: CFrame
        self.RightClavicle = None  # type: Instance | undefined
        self.RightClavicleRangeMax = None  # type: Vector3
        self.RightClavicleRangeMin = None  # type: Vector3
        self.RightClavicleSize = None  # type: float
        self.RightClavicleTposeAdjustment = None  # type: CFrame
        self.RightElbow = None  # type: Instance | undefined
        self.RightElbowRangeMax = None  # type: Vector3
        self.RightElbowRangeMin = None  # type: Vector3
        self.RightElbowSize = None  # type: float
        self.RightElbowTposeAdjustment = None  # type: CFrame
        self.RightHip = None  # type: Instance | undefined
        self.RightHipRangeMax = None  # type: Vector3
        self.RightHipRangeMin = None  # type: Vector3
        self.RightHipSize = None  # type: float
        self.RightHipTposeAdjustment = None  # type: CFrame
        self.RightKnee = None  # type: Instance | undefined
        self.RightKneeRangeMax = None  # type: Vector3
        self.RightKneeRangeMin = None  # type: Vector3
        self.RightKneeSize = None  # type: float
        self.RightKneeTposeAdjustment = None  # type: CFrame
        self.RightShoulder = None  # type: Instance | undefined
        self.RightShoulderRangeMax = None  # type: Vector3
        self.RightShoulderRangeMin = None  # type: Vector3
        self.RightShoulderSize = None  # type: float
        self.RightShoulderTposeAdjustment = None  # type: CFrame
        self.RightToes = None  # type: Instance | undefined
        self.RightToesRangeMax = None  # type: Vector3
        self.RightToesRangeMin = None  # type: Vector3
        self.RightToesSize = None  # type: float
        self.RightToesTposeAdjustment = None  # type: CFrame
        self.RightWrist = None  # type: Instance | undefined
        self.RightWristRangeMax = None  # type: Vector3
        self.RightWristRangeMin = None  # type: Vector3
        self.RightWristSize = None  # type: float
        self.RightWristTposeAdjustment = None  # type: CFrame
        self.Root = None  # type: Instance | undefined
        self.RootRangeMax = None  # type: Vector3
        self.RootRangeMin = None  # type: Vector3
        self.RootSize = None  # type: float
        self.RootTposeAdjustment = None  # type: CFrame
        self.Waist = None  # type: Instance | undefined
        self.WaistRangeMax = None  # type: Vector3
        self.WaistRangeMin = None  # type: Vector3
        self.WaistSize = None  # type: float
        self.WaistTposeAdjustment = None  # type: CFrame

class IKControl:
    def __init__(self):
        self._nominal_IKControl = None  # type: unique symbol
        self.ChainRoot = None  # type: Instance | undefined
        self.Enabled = None  # type: bool
        self.EndEffector = None  # type: Instance | undefined
        self.EndEffectorOffset = None  # type: CFrame
        self.Offset = None  # type: CFrame
        self.Pole = None  # type: Instance | undefined
        self.Priority = None  # type: float
        self.SmoothTime = None  # type: float
        self.Target = None  # type: Instance | undefined
        self.Type = None  # type: Enum.IKControlType
        self.Weight = None  # type: float

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
        self.UploadComplete = None  # type: RBXScriptSignal<(results: object) => void>
        self.UploadProgress = None  # type: RBXScriptSignal<(progressRatio: float) => void>

class AssetImportSession:
    def __init__(self):
        self._nominal_AssetImportSession = None  # type: unique symbol

class IncrementalPatchBuilder:
    def __init__(self):
        self._nominal_IncrementalPatchBuilder = None  # type: unique symbol
        self.AddPathsToBundle = None  # type: bool
        self.BuildDebouncePeriod = None  # type: float
        self.HighCompression = None  # type: bool
        self.SerializePatch = None  # type: bool
        self.ZstdCompression = None  # type: bool

class InputAction:
    def __init__(self):
        self._nominal_InputAction = None  # type: unique symbol
        self.Enabled = None  # type: bool
        self.Type = None  # type: Enum.InputActionType
        self.Pressed = None  # type: RBXScriptSignal<() => void>
        self.Released = None  # type: RBXScriptSignal<() => void>
        self.StateChanged = None  # type: RBXScriptSignal<(value: unknown) => void>

class InputBinding:
    def __init__(self):
        self._nominal_InputBinding = None  # type: unique symbol
        self.Down = None  # type: Enum.KeyCode
        self.KeyCode = None  # type: Enum.KeyCode
        self.Left = None  # type: Enum.KeyCode
        self.PressedThreshold = None  # type: float
        self.ReleasedThreshold = None  # type: float
        self.Right = None  # type: Enum.KeyCode
        self.Scale = None  # type: float
        self.UIButton = None  # type: GuiButton | undefined
        self.Up = None  # type: Enum.KeyCode
        self.Vector2Scale = None  # type: Vector2

class InputContext:
    def __init__(self):
        self._nominal_InputContext = None  # type: unique symbol
        self.Enabled = None  # type: bool
        self.Priority = None  # type: float
        self.Sink = None  # type: bool

class InputObject:
    def __init__(self):
        self._nominal_InputObject = None  # type: unique symbol
        self.Delta = None  # type: Vector3
        self.KeyCode = None  # type: Enum.KeyCode
        self.Position = None  # type: Vector3
        self.UserInputState = None  # type: Enum.UserInputState
        self.UserInputType = None  # type: Enum.UserInputType

class InsertService:
    def __init__(self):
        self._nominal_InsertService = None  # type: unique symbol
        self.AllowInsertFreeModels = None  # type: bool
        self.InternalDelete = None  # type: RBXScriptSignal<(instance: Instance) => void>

class InternalSyncItem:
    def __init__(self):
        self._nominal_InternalSyncItem = None  # type: unique symbol

class InternalSyncService:
    def __init__(self):
        self._nominal_InternalSyncService = None  # type: unique symbol

class JointInstance:
    def __init__(self):
        self._nominal_JointInstance = None  # type: unique symbol
        self.Active = None  # type: bool
        self.C0 = None  # type: CFrame
        self.C1 = None  # type: CFrame
        self.Enabled = None  # type: bool
        self.Part0 = None  # type: BasePart | undefined
        self.Part1 = None  # type: BasePart | undefined

class DynamicRotate:
    def __init__(self):
        self._nominal_DynamicRotate = None  # type: unique symbol
        self.BaseAngle = None  # type: float

class RotateP:
    def __init__(self):
        self._nominal_RotateP = None  # type: unique symbol

class RotateV:
    def __init__(self):
        self._nominal_RotateV = None  # type: unique symbol

class Glue:
    def __init__(self):
        self._nominal_Glue = None  # type: unique symbol
        self.F0 = None  # type: Vector3
        self.F1 = None  # type: Vector3
        self.F2 = None  # type: Vector3
        self.F3 = None  # type: Vector3

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
        self.CurrentAngle = None  # type: float
        self.DesiredAngle = None  # type: float
        self.MaxVelocity = None  # type: float

class Motor6D:
    def __init__(self):
        self._nominal_Motor6D = None  # type: unique symbol
        self.Transform = None  # type: CFrame

class Rotate:
    def __init__(self):
        self._nominal_Rotate = None  # type: unique symbol

class Snap:
    def __init__(self):
        self._nominal_Snap = None  # type: unique symbol

class VelocityMotor:
    def __init__(self):
        self._nominal_VelocityMotor = None  # type: unique symbol
        self.CurrentAngle = None  # type: float
        self.DesiredAngle = None  # type: float
        self.Hole = None  # type: Hole | undefined
        self.MaxVelocity = None  # type: float

class Weld:
    def __init__(self):
        self._nominal_Weld = None  # type: unique symbol

class JointsService:
    def __init__(self):
        self._nominal_JointsService = None  # type: unique symbol

class Keyframe:
    def __init__(self):
        self._nominal_Keyframe = None  # type: unique symbol
        self.Time = None  # type: float

class KeyframeMarker:
    def __init__(self):
        self._nominal_KeyframeMarker = None  # type: unique symbol
        self.Value = None  # type: str

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
        self.Brightness = None  # type: float
        self.Color = None  # type: Color3
        self.Enabled = None  # type: bool
        self.Shadows = None  # type: bool

class PointLight:
    def __init__(self):
        self._nominal_PointLight = None  # type: unique symbol
        self.Range = None  # type: float

class SpotLight:
    def __init__(self):
        self._nominal_SpotLight = None  # type: unique symbol
        self.Angle = None  # type: float
        self.Face = None  # type: Enum.NormalId
        self.Range = None  # type: float

class SurfaceLight:
    def __init__(self):
        self._nominal_SurfaceLight = None  # type: unique symbol
        self.Angle = None  # type: float
        self.Face = None  # type: Enum.NormalId
        self.Range = None  # type: float

class Lighting:
    def __init__(self):
        self._nominal_Lighting = None  # type: unique symbol
        self.Ambient = None  # type: Color3
        self.Brightness = None  # type: float
        self.ClockTime = None  # type: float
        self.ColorShift_Bottom = None  # type: Color3
        self.ColorShift_Top = None  # type: Color3
        self.EnvironmentDiffuseScale = None  # type: float
        self.EnvironmentSpecularScale = None  # type: float
        self.ExposureCompensation = None  # type: float
        self.FogColor = None  # type: Color3
        self.FogEnd = None  # type: float
        self.FogStart = None  # type: float
        self.GeographicLatitude = None  # type: float
        self.GlobalShadows = None  # type: bool
        self.OutdoorAmbient = None  # type: Color3
        self.Outlines = None  # type: bool
        self.ShadowColor = None  # type: Color3
        self.ShadowSoftness = None  # type: float
        self.TimeOfDay = None  # type: str
        self.LightingChanged = None  # type: RBXScriptSignal<(skyChanged: bool) => void>

class LinkingService:
    def __init__(self):
        self._nominal_LinkingService = None  # type: unique symbol

class LiveScriptingService:
    def __init__(self):
        self._nominal_LiveScriptingService = None  # type: unique symbol

class LiveSyncService:
    def __init__(self):
        self._nominal_LiveSyncService = None  # type: unique symbol
        self.HasSyncedInstances = None  # type: bool
        self.SyncStatusChanged = None  # type: RBXScriptSignal<(instance: Instance) => void>

class LocalizationService:
    def __init__(self):
        self._nominal_LocalizationService = None  # type: unique symbol
        self.RobloxLocaleId = None  # type: str
        self.SystemLocaleId = None  # type: str

class LocalizationTable:
    def __init__(self):
        self._nominal_LocalizationTable = None  # type: unique symbol
        self.DevelopmentLanguage = None  # type: str
        self.Root = None  # type: Instance | undefined
        self.SourceLocaleId = None  # type: str

class CloudLocalizationTable:
    def __init__(self):
        self._nominal_CloudLocalizationTable = None  # type: unique symbol

class LodDataEntity:
    def __init__(self):
        self._nominal_LodDataEntity = None  # type: unique symbol
        self.EntityLodEnabled = None  # type: bool

class LodDataService:
    def __init__(self):
        self._nominal_LodDataService = None  # type: unique symbol

class LogReporterService:
    def __init__(self):
        self._nominal_LogReporterService = None  # type: unique symbol

class LogService:
    def __init__(self):
        self._nominal_LogService = None  # type: unique symbol
        self.MessageOut = None  # type: RBXScriptSignal<(message: str, messageType: Enum.MessageType) => void>

class LuaSourceContainer:
    def __init__(self):
        self._nominal_LuaSourceContainer = None  # type: unique symbol

class AuroraScript:
    def __init__(self):
        self._nominal_AuroraScript = None  # type: unique symbol

class BaseScript:
    def __init__(self):
        self._nominal_BaseScript = None  # type: unique symbol
        self.Disabled = None  # type: bool
        self.Enabled = None  # type: bool
        self.LinkedSource = None  # type: ContentId

class Script:
    def __init__(self):
        self._nominal_Script = None  # type: unique symbol
        self.Source = None  # type: ProtectedString

class LocalScript:
    def __init__(self):
        self._nominal_LocalScript = None  # type: unique symbol

class ModuleScript:
    def __init__(self):
        self._nominal_ModuleScript = None  # type: unique symbol
        self.LinkedSource = None  # type: ContentId
        self.Source = None  # type: ProtectedString

class LuauScriptAnalyzerService:
    def __init__(self):
        self._nominal_LuauScriptAnalyzerService = None  # type: unique symbol

class MLModelDeliveryService:
    def __init__(self):
        self._nominal_MLModelDeliveryService = None  # type: unique symbol

class MarkerCurve:
    def __init__(self):
        self._nominal_MarkerCurve = None  # type: unique symbol
        self.Length = None  # type: float

class MarketplaceService:
    def __init__(self):
        self._nominal_MarketplaceService = None  # type: unique symbol
        self.PromptBulkPurchaseFinished = None  # type: RBXScriptSignal<(player: Player, status: Enum.MarketplaceBulkPurchasePromptStatus, results: PromptBulkPurchaseFinishedResults) => void>
        self.PromptBundlePurchaseFinished = None  # type: RBXScriptSignal<(player: Player, bundleId: float, wasPurchased: bool) => void>
        self.PromptGamePassPurchaseFinished = None  # type: RBXScriptSignal<(player: Player, gamePassId: float, wasPurchased: bool) => void>
        self.PromptPremiumPurchaseFinished = None  # type: RBXScriptSignal<() => void>
        self.PromptProductPurchaseFinished = None  # type: RBXScriptSignal<(userId: float, productId: float, isPurchased: bool) => void>
        self.PromptPurchaseFinished = None  # type: RBXScriptSignal<(player: Player, assetId: float, isPurchased: bool) => void>
        self.PromptSubscriptionPurchaseFinished = None  # type: RBXScriptSignal<(user: Player, subscriptionId: str, didTryPurchasing: bool) => void>
        self.ProcessReceipt = None  # type: ((receiptInfo: ReceiptInfo) => Enum.ProductPurchaseDecision) | undefined

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
        self.CustomPhysicalProperties = None  # type: PhysicalProperties
        self.MaterialPattern = None  # type: Enum.MaterialPattern
        self.StudsPerTile = None  # type: float

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
        self.Hit = None  # type: CFrame
        self.Icon = None  # type: ContentId
        self.Origin = None  # type: CFrame
        self.Target = None  # type: BasePart | undefined
        self.TargetFilter = None  # type: Instance | undefined
        self.TargetSurface = None  # type: Enum.NormalId
        self.UnitRay = None  # type: Ray
        self.ViewSizeX = None  # type: float
        self.ViewSizeY = None  # type: float
        self.X = None  # type: float
        self.Y = None  # type: float
        self.Button1Down = None  # type: RBXScriptSignal<() => void>
        self.Button1Up = None  # type: RBXScriptSignal<() => void>
        self.Button2Down = None  # type: RBXScriptSignal<() => void>
        self.Button2Up = None  # type: RBXScriptSignal<() => void>
        self.Idle = None  # type: RBXScriptSignal<() => void>
        self.KeyDown = None  # type: RBXScriptSignal<(key: str) => void>
        self.KeyUp = None  # type: RBXScriptSignal<(key: str) => void>
        self.Move = None  # type: RBXScriptSignal<() => void>
        self.WheelBackward = None  # type: RBXScriptSignal<() => void>
        self.WheelForward = None  # type: RBXScriptSignal<() => void>

class PlayerMouse:
    def __init__(self):
        self._nominal_PlayerMouse = None  # type: unique symbol

class NetworkMarker:
    def __init__(self):
        self._nominal_NetworkMarker = None  # type: unique symbol
        self.Received = None  # type: RBXScriptSignal<() => void>

class NoCollisionConstraint:
    def __init__(self):
        self._nominal_NoCollisionConstraint = None  # type: unique symbol
        self.Enabled = None  # type: bool
        self.Part0 = None  # type: BasePart | undefined
        self.Part1 = None  # type: BasePart | undefined

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
        self.Anchored = None  # type: bool
        self.AssemblyAngularVelocity = None  # type: Vector3
        self.AssemblyCenterOfMass = None  # type: Vector3
        self.AssemblyLinearVelocity = None  # type: Vector3
        self.AssemblyMass = None  # type: float
        self.AssemblyRootPart = None  # type: BasePart | undefined
        self.AudioCanCollide = None  # type: bool
        self.BackParamA = None  # type: float
        self.BackParamB = None  # type: float
        self.BackSurface = None  # type: Enum.SurfaceType
        self.BackSurfaceInput = None  # type: Enum.InputType
        self.BottomParamA = None  # type: float
        self.BottomParamB = None  # type: float
        self.BottomSurface = None  # type: Enum.SurfaceType
        self.BottomSurfaceInput = None  # type: Enum.InputType
        self.BrickColor = None  # type: BrickColor
        self.CFrame = None  # type: CFrame
        self.CanCollide = None  # type: bool
        self.CanQuery = None  # type: bool
        self.CanTouch = None  # type: bool
        self.CastShadow = None  # type: bool
        self.CenterOfMass = None  # type: Vector3
        self.CollisionGroup = None  # type: str
        self.CollisionGroupId = None  # type: float
        self.Color = None  # type: Color3
        self.CurrentPhysicalProperties = None  # type: PhysicalProperties
        self.CustomPhysicalProperties = None  # type: PhysicalProperties | undefined
        self.Elasticity = None  # type: float
        self.EnableFluidForces = None  # type: bool
        self.ExtentsCFrame = None  # type: CFrame
        self.ExtentsSize = None  # type: Vector3
        self.Friction = None  # type: float
        self.FrontParamA = None  # type: float
        self.FrontParamB = None  # type: float
        self.FrontSurface = None  # type: Enum.SurfaceType
        self.FrontSurfaceInput = None  # type: Enum.InputType
        self.LeftParamA = None  # type: float
        self.LeftParamB = None  # type: float
        self.LeftSurface = None  # type: Enum.SurfaceType
        self.LeftSurfaceInput = None  # type: Enum.InputType
        self.LocalTransparencyModifier = None  # type: float
        self.Locked = None  # type: bool
        self.Mass = None  # type: float
        self.Massless = None  # type: bool
        self.Material = None  # type: Enum.Material
        self.MaterialVariant = None  # type: str
        self.Orientation = None  # type: Vector3
        self.PivotOffset = None  # type: CFrame
        self.Position = None  # type: Vector3
        self.ReceiveAge = None  # type: float
        self.Reflectance = None  # type: float
        self.ResizeIncrement = None  # type: float
        self.ResizeableFaces = None  # type: Faces
        self.RightParamA = None  # type: float
        self.RightParamB = None  # type: float
        self.RightSurface = None  # type: Enum.SurfaceType
        self.RightSurfaceInput = None  # type: Enum.InputType
        self.RootPriority = None  # type: float
        self.RotVelocity = None  # type: Vector3
        self.Rotation = None  # type: Vector3
        self.Size = None  # type: Vector3
        self.SpecificGravity = None  # type: float
        self.TopParamA = None  # type: float
        self.TopParamB = None  # type: float
        self.TopSurface = None  # type: Enum.SurfaceType
        self.TopSurfaceInput = None  # type: Enum.InputType
        self.Transparency = None  # type: float
        self.Velocity = None  # type: Vector3
        self.LocalSimulationTouched = None  # type: RBXScriptSignal<(part: BasePart) => void>
        self.OutfitChanged = None  # type: RBXScriptSignal<() => void>
        self.StoppedTouching = None  # type: RBXScriptSignal<(otherPart: BasePart) => void>
        self.TouchEnded = None  # type: RBXScriptSignal<(otherPart: BasePart) => void>
        self.Touched = None  # type: RBXScriptSignal<(otherPart: BasePart) => void>

class CornerWedgePart:
    def __init__(self):
        self._nominal_CornerWedgePart = None  # type: unique symbol

class FormFactorPart:
    def __init__(self):
        self._nominal_FormFactorPart = None  # type: unique symbol
        self.FormFactor = None  # type: Enum.FormFactor

class Part:
    def __init__(self):
        self._nominal_Part = None  # type: unique symbol
        self.Shape = None  # type: Enum.PartType

class Platform:
    def __init__(self):
        self._nominal_Platform = None  # type: unique symbol
        self.RemoteCreateMotor6D = None  # type: RBXScriptSignal<(humanoid: Humanoid) => void>
        self.RemoteDestroyMotor6D = None  # type: RBXScriptSignal<() => void>

class Seat:
    def __init__(self):
        self._nominal_Seat = None  # type: unique symbol
        self.Disabled = None  # type: bool
        self.Occupant = None  # type: Humanoid | undefined
        self.RemoteCreateSeatWeld = None  # type: RBXScriptSignal<(humanoid: Humanoid) => void>
        self.RemoteDestroySeatWeld = None  # type: RBXScriptSignal<() => void>

class SkateboardPlatform:
    def __init__(self):
        self._nominal_SkateboardPlatform = None  # type: unique symbol
        self.Controller = None  # type: SkateboardController | undefined
        self.ControllingHumanoid = None  # type: Humanoid | undefined
        self.Steer = None  # type: float
        self.StickyWheels = None  # type: bool
        self.Throttle = None  # type: float
        self.Equipped = None  # type: RBXScriptSignal<(humanoid: Humanoid, skateboardController: SkateboardController) => void>
        self.MoveStateChanged = None  # type: RBXScriptSignal<(newState: Enum.MoveState, oldState: Enum.MoveState) => void>
        self.RemoteCreateMotor6D = None  # type: RBXScriptSignal<(humanoid: Humanoid) => void>
        self.RemoteDestroyMotor6D = None  # type: RBXScriptSignal<() => void>
        self.Unequipped = None  # type: RBXScriptSignal<(humanoid: Humanoid) => void>

class SpawnLocation:
    def __init__(self):
        self._nominal_SpawnLocation = None  # type: unique symbol
        self.AllowTeamChangeOnTouch = None  # type: bool
        self.Duration = None  # type: float
        self.Enabled = None  # type: bool
        self.Neutral = None  # type: bool
        self.TeamColor = None  # type: BrickColor

class WedgePart:
    def __init__(self):
        self._nominal_WedgePart = None  # type: unique symbol

class Terrain:
    def __init__(self):
        self._nominal_Terrain = None  # type: unique symbol
        self.IsSmooth = None  # type: bool
        self.MaxExtents = None  # type: Region3int16
        self.WaterColor = None  # type: Color3
        self.WaterReflectance = None  # type: float
        self.WaterTransparency = None  # type: float
        self.WaterWaveSize = None  # type: float
        self.WaterWaveSpeed = None  # type: float

class TriangleMeshPart:
    def __init__(self):
        self._nominal_TriangleMeshPart = None  # type: unique symbol
        self.MeshSize = None  # type: Vector3

class MeshPart:
    def __init__(self):
        self._nominal_MeshPart = None  # type: unique symbol
        self.TextureContent = None  # type: Content
        self.TextureID = None  # type: ContentId

class PartOperation:
    def __init__(self):
        self._nominal_PartOperation = None  # type: unique symbol
        self.TriangleCount = None  # type: float
        self.UsePartColor = None  # type: bool

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
        self.Style = None  # type: Enum.Style

class VehicleSeat:
    def __init__(self):
        self._nominal_VehicleSeat = None  # type: unique symbol
        self.AreHingesDetected = None  # type: float
        self.Disabled = None  # type: bool
        self.HeadsUpDisplay = None  # type: bool
        self.MaxSpeed = None  # type: float
        self.Occupant = None  # type: Humanoid | undefined
        self.Steer = None  # type: float
        self.SteerFloat = None  # type: float
        self.Throttle = None  # type: float
        self.ThrottleFloat = None  # type: float
        self.Torque = None  # type: float
        self.TurnSpeed = None  # type: float
        self.RemoteCreateSeatWeld = None  # type: RBXScriptSignal<(humanoid: Instance) => void>
        self.RemoteDestroySeatWeld = None  # type: RBXScriptSignal<() => void>

class Camera:
    def __init__(self):
        self._nominal_Camera = None  # type: unique symbol
        self.CFrame = None  # type: CFrame
        self.CameraSubject = None  # type: Humanoid | BasePart | undefined
        self.CameraType = None  # type: Enum.CameraType
        self.CoordinateFrame = None  # type: CFrame
        self.DiagonalFieldOfView = None  # type: float
        self.FieldOfView = None  # type: float
        self.FieldOfViewMode = None  # type: Enum.FieldOfViewMode
        self.Focus = None  # type: CFrame
        self.HeadLocked = None  # type: bool
        self.HeadScale = None  # type: float
        self.MaxAxisFieldOfView = None  # type: float
        self.NearPlaneZ = None  # type: float
        self.VRTiltAndRollEnabled = None  # type: bool
        self.ViewportSize = None  # type: Vector2
        self.InterpolationFinished = None  # type: RBXScriptSignal<() => void>

class Model:
    def __init__(self):
        self._nominal_Model = None  # type: unique symbol
        self.ModelStreamingMode = None  # type: Enum.ModelStreamingMode
        self.PrimaryPart = None  # type: BasePart | undefined
        self.WorldPivot = None  # type: CFrame

class Actor:
    def __init__(self):
        self._nominal_Actor = None  # type: unique symbol

class BackpackItem:
    def __init__(self):
        self._nominal_BackpackItem = None  # type: unique symbol
        self.TextureId = None  # type: ContentId

class Tool:
    def __init__(self):
        self._nominal_Tool = None  # type: unique symbol
        self.CanBeDropped = None  # type: bool
        self.Enabled = None  # type: bool
        self.Grip = None  # type: CFrame
        self.GripForward = None  # type: Vector3
        self.GripPos = None  # type: Vector3
        self.GripRight = None  # type: Vector3
        self.GripUp = None  # type: Vector3
        self.ManualActivationOnly = None  # type: bool
        self.RequiresHandle = None  # type: bool
        self.ToolTip = None  # type: str
        self.Activated = None  # type: RBXScriptSignal<() => void>
        self.Deactivated = None  # type: RBXScriptSignal<() => void>
        self.Equipped = None  # type: RBXScriptSignal<(mouse: Mouse) => void>
        self.Unequipped = None  # type: RBXScriptSignal<() => void>

class WorldRoot:
    def __init__(self):
        self._nominal_WorldRoot = None  # type: unique symbol

class Workspace:
    def __init__(self):
        self._nominal_Workspace = None  # type: unique symbol
        self.AirDensity = None  # type: float
        self.AllowThirdPartySales = None  # type: bool
        self.ClientAnimatorThrottling = None  # type: Enum.ClientAnimatorThrottlingMode
        self.CurrentCamera = None  # type: Camera | undefined
        self.DistributedGameTime = None  # type: float
        self.GlobalWind = None  # type: Vector3
        self.Gravity = None  # type: float
        self.InsertPoint = None  # type: Vector3
        self.Retargeting = None  # type: Enum.AnimatorRetargetingMode
        self.Terrain = None  # type: Terrain
        self.PersistentLoaded = None  # type: RBXScriptSignal<(player: Player) => void>

class WorldModel:
    def __init__(self):
        self._nominal_WorldModel = None  # type: unique symbol

class PackageLink:
    def __init__(self):
        self._nominal_PackageLink = None  # type: unique symbol
        self.PackageId = None  # type: ContentId

class PackageUIService:
    def __init__(self):
        self._nominal_PackageUIService = None  # type: unique symbol

class Pages:
    def __init__(self):
        self._nominal_Pages = None  # type: unique symbol
        self.IsFinished = None  # type: bool

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
        self.Cursor = None  # type: str

class DataStoreListingPages:
    def __init__(self):
        self._nominal_DataStoreListingPages = None  # type: unique symbol
        self.Cursor = None  # type: str

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
        self.Acceleration = None  # type: Vector3
        self.Brightness = None  # type: float
        self.Color = None  # type: ColorSequence
        self.Drag = None  # type: float
        self.EmissionDirection = None  # type: Enum.NormalId
        self.Enabled = None  # type: bool
        self.FlipbookFramerate = None  # type: NumberRange
        self.FlipbookIncompatible = None  # type: str
        self.FlipbookLayout = None  # type: Enum.ParticleFlipbookLayout
        self.FlipbookMode = None  # type: Enum.ParticleFlipbookMode
        self.FlipbookStartRandom = None  # type: bool
        self.Lifetime = None  # type: NumberRange
        self.LightEmission = None  # type: float
        self.LightInfluence = None  # type: float
        self.LocalTransparencyModifier = None  # type: float
        self.LockedToPart = None  # type: bool
        self.Orientation = None  # type: Enum.ParticleOrientation
        self.Rate = None  # type: float
        self.RotSpeed = None  # type: NumberRange
        self.Rotation = None  # type: NumberRange
        self.Shape = None  # type: Enum.ParticleEmitterShape
        self.ShapeInOut = None  # type: Enum.ParticleEmitterShapeInOut
        self.ShapePartial = None  # type: float
        self.ShapeStyle = None  # type: Enum.ParticleEmitterShapeStyle
        self.Size = None  # type: NumberSequence
        self.Speed = None  # type: NumberRange
        self.SpreadAngle = None  # type: Vector2
        self.Squash = None  # type: NumberSequence
        self.Texture = None  # type: ContentId
        self.TimeScale = None  # type: float
        self.Transparency = None  # type: NumberSequence
        self.VelocityInheritance = None  # type: float
        self.VelocitySpread = None  # type: float
        self.WindAffectsDrag = None  # type: bool
        self.ZOffset = None  # type: float
        self.OnClearRequested = None  # type: RBXScriptSignal<() => void>
        self.OnEmitRequested = None  # type: RBXScriptSignal<(particleCount: float) => void>

class PatchBundlerFileWatch:
    def __init__(self):
        self._nominal_PatchBundlerFileWatch = None  # type: unique symbol

class PatchMapping:
    def __init__(self):
        self._nominal_PatchMapping = None  # type: unique symbol
        self.FlattenTree = None  # type: bool
        self.PatchId = None  # type: str
        self.TargetPath = None  # type: str

class Path:
    def __init__(self):
        self._nominal_Path = None  # type: unique symbol
        self.Status = None  # type: Enum.PathStatus
        self.Blocked = None  # type: RBXScriptSignal<(blockedWaypointIdx: float) => void>
        self.Unblocked = None  # type: RBXScriptSignal<(unblockedWaypointIdx: float) => void>

class PathfindingLink:
    def __init__(self):
        self._nominal_PathfindingLink = None  # type: unique symbol
        self.Attachment0 = None  # type: Attachment | undefined
        self.Attachment1 = None  # type: Attachment | undefined
        self.IsBidirectional = None  # type: bool
        self.Label = None  # type: str

class PathfindingModifier:
    def __init__(self):
        self._nominal_PathfindingModifier = None  # type: unique symbol
        self.Label = None  # type: str
        self.PassThrough = None  # type: bool

class PathfindingService:
    def __init__(self):
        self._nominal_PathfindingService = None  # type: unique symbol
        self.EmptyCutoff = None  # type: float

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
        self.AccountAge = None  # type: float
        self.AutoJumpEnabled = None  # type: bool
        self.CameraMaxZoomDistance = None  # type: float
        self.CameraMinZoomDistance = None  # type: float
        self.CameraMode = None  # type: Enum.CameraMode
        self.CanLoadCharacterAppearance = None  # type: bool
        self.Character = None  # type: Model | undefined
        self.CharacterAppearance = None  # type: str
        self.CharacterAppearanceId = None  # type: float
        self.DataComplexity = None  # type: float
        self.DataReady = None  # type: bool
        self.DevCameraOcclusionMode = None  # type: Enum.DevCameraOcclusionMode
        self.DevComputerCameraMode = None  # type: Enum.DevComputerCameraMovementMode
        self.DevComputerMovementMode = None  # type: Enum.DevComputerMovementMode
        self.DevEnableMouseLock = None  # type: bool
        self.DevTouchCameraMode = None  # type: Enum.DevTouchCameraMovementMode
        self.DevTouchMovementMode = None  # type: Enum.DevTouchMovementMode
        self.DisplayName = None  # type: str
        self.FollowUserId = None  # type: float
        self.HasVerifiedBadge = None  # type: bool
        self.HealthDisplayDistance = None  # type: float
        self.LocaleId = None  # type: str
        self.MembershipType = None  # type: Enum.MembershipType
        self.NameDisplayDistance = None  # type: float
        self.Neutral = None  # type: bool
        self.ReplicationFocus = None  # type: BasePart | undefined
        self.RespawnLocation = None  # type: SpawnLocation | undefined
        self.Team = None  # type: Team | undefined
        self.TeamColor = None  # type: BrickColor
        self.UserId = None  # type: float
        self.CharacterAdded = None  # type: RBXScriptSignal<(character: Model) => void>
        self.CharacterAppearanceLoaded = None  # type: RBXScriptSignal<(character: Model) => void>
        self.CharacterRemoving = None  # type: RBXScriptSignal<(character: Model) => void>
        self.Chatted = None  # type: RBXScriptSignal<(message: str, recipient?: Player) => void>
        self.Idled = None  # type: RBXScriptSignal<(time: float) => void>
        self.OnTeleport = None  # type: RBXScriptSignal<(teleportState: Enum.TeleportState, placeId: float, spawnName: str) => void>
        self.Name = None  # type: str

class PlayerData:
    def __init__(self):
        self._nominal_PlayerData = None  # type: unique symbol

class PlayerDataRecord:
    def __init__(self):
        self._nominal_PlayerDataRecord = None  # type: unique symbol
        self.CreatedTime = None  # type: float
        self.DefaultRecordName = None  # type: bool
        self.Dirty = None  # type: bool
        self.Error = None  # type: Enum.PlayerDataErrorState
        self.FlushedTime = None  # type: float
        self.LoadedTime = None  # type: float
        self.ModifiedTime = None  # type: float
        self.NewRecord = None  # type: bool
        self.Readable = None  # type: bool
        self.RecordName = None  # type: str
        self.Writable = None  # type: bool
        self.Changed = None  # type: RBXScriptSignal<(key: str, value: unknown) => void>
        self.Flushed = None  # type: RBXScriptSignal<(flushState: bool, error?: str) => void>
        self.Loaded = None  # type: RBXScriptSignal<(success: bool, error?: str) => void>

class PlayerDataRecordConfig:
    def __init__(self):
        self._nominal_PlayerDataRecordConfig = None  # type: unique symbol
        self.RecordName = None  # type: str

class PlayerDataService:
    def __init__(self):
        self._nominal_PlayerDataService = None  # type: unique symbol
        self.LoadFailureBehavior = None  # type: Enum.PlayerDataLoadFailureBehavior

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
        self.BubbleChat = None  # type: bool
        self.CharacterAutoLoads = None  # type: bool
        self.ClassicChat = None  # type: bool
        self.LocalPlayer = None  # type: Player
        self.MaxPlayers = None  # type: float
        self.NumPlayers = None  # type: float
        self.PreferredPlayers = None  # type: float
        self.RespawnTime = None  # type: float
        self.PlayerAdded = None  # type: RBXScriptSignal<(player: Player) => void>
        self.PlayerMembershipChanged = None  # type: RBXScriptSignal<(player: Player) => void>
        self.PlayerRemoving = None  # type: RBXScriptSignal<(player: Player) => void>
        self.UserSubscriptionStatusChanged = None  # type: RBXScriptSignal<(user: Player, subscriptionId: str) => void>

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
        self.EasingDirection = None  # type: Enum.PoseEasingDirection
        self.EasingStyle = None  # type: Enum.PoseEasingStyle
        self.Weight = None  # type: float

class NumberPose:
    def __init__(self):
        self._nominal_NumberPose = None  # type: unique symbol
        self.Value = None  # type: float

class Pose:
    def __init__(self):
        self._nominal_Pose = None  # type: unique symbol
        self.CFrame = None  # type: CFrame
        self.MaskWeight = None  # type: float

class PostEffect:
    def __init__(self):
        self._nominal_PostEffect = None  # type: unique symbol
        self.Enabled = None  # type: bool

class BloomEffect:
    def __init__(self):
        self._nominal_BloomEffect = None  # type: unique symbol
        self.Intensity = None  # type: float
        self.Size = None  # type: float
        self.Threshold = None  # type: float

class BlurEffect:
    def __init__(self):
        self._nominal_BlurEffect = None  # type: unique symbol
        self.Size = None  # type: float

class ColorCorrectionEffect:
    def __init__(self):
        self._nominal_ColorCorrectionEffect = None  # type: unique symbol
        self.Brightness = None  # type: float
        self.Contrast = None  # type: float
        self.Saturation = None  # type: float
        self.TintColor = None  # type: Color3

class ColorGradingEffect:
    def __init__(self):
        self._nominal_ColorGradingEffect = None  # type: unique symbol
        self.TonemapperPreset = None  # type: Enum.TonemapperPreset

class DepthOfFieldEffect:
    def __init__(self):
        self._nominal_DepthOfFieldEffect = None  # type: unique symbol
        self.FarIntensity = None  # type: float
        self.FocusDistance = None  # type: float
        self.InFocusRadius = None  # type: float
        self.NearIntensity = None  # type: float

class SunRaysEffect:
    def __init__(self):
        self._nominal_SunRaysEffect = None  # type: unique symbol
        self.Intensity = None  # type: float
        self.Spread = None  # type: float

class ProcessInstancePhysicsService:
    def __init__(self):
        self._nominal_ProcessInstancePhysicsService = None  # type: unique symbol

class ProximityPrompt:
    def __init__(self):
        self._nominal_ProximityPrompt = None  # type: unique symbol
        self.ActionText = None  # type: str
        self.AutoLocalize = None  # type: bool
        self.ClickablePrompt = None  # type: bool
        self.Enabled = None  # type: bool
        self.Exclusivity = None  # type: Enum.ProximityPromptExclusivity
        self.GamepadKeyCode = None  # type: Enum.KeyCode
        self.HoldDuration = None  # type: float
        self.KeyboardKeyCode = None  # type: Enum.KeyCode
        self.MaxActivationDistance = None  # type: float
        self.ObjectText = None  # type: str
        self.RequiresLineOfSight = None  # type: bool
        self.RootLocalizationTable = None  # type: LocalizationTable | undefined
        self.Style = None  # type: Enum.ProximityPromptStyle
        self.UIOffset = None  # type: Vector2
        self.PromptButtonHoldBegan = None  # type: RBXScriptSignal<(playerWhoTriggered: Player) => void>
        self.PromptButtonHoldEnded = None  # type: RBXScriptSignal<(playerWhoTriggered: Player) => void>
        self.PromptHidden = None  # type: RBXScriptSignal<() => void>
        self.PromptShown = None  # type: RBXScriptSignal<(inputType: Enum.ProximityPromptInputType) => void>
        self.TriggerEnded = None  # type: RBXScriptSignal<(playerWhoTriggered: Player) => void>
        self.Triggered = None  # type: RBXScriptSignal<(playerWhoTriggered: Player) => void>

class ProximityPromptService:
    def __init__(self):
        self._nominal_ProximityPromptService = None  # type: unique symbol
        self.Enabled = None  # type: bool
        self.MaxPromptsVisible = None  # type: float
        self.PromptButtonHoldBegan = None  # type: RBXScriptSignal<(prompt: ProximityPrompt, playerWhoTriggered: Player) => void>
        self.PromptButtonHoldEnded = None  # type: RBXScriptSignal<(prompt: ProximityPrompt, playerWhoTriggered: Player) => void>
        self.PromptHidden = None  # type: RBXScriptSignal<(prompt: ProximityPrompt) => void>
        self.PromptShown = None  # type: RBXScriptSignal<(prompt: ProximityPrompt, inputType: Enum.ProximityPromptInputType) => void>
        self.PromptTriggerEnded = None  # type: RBXScriptSignal<(prompt: ProximityPrompt, playerWhoTriggered: Player) => void>
        self.PromptTriggered = None  # type: RBXScriptSignal<(prompt: ProximityPrompt, playerWhoTriggered: Player) => void>

class PublishService:
    def __init__(self):
        self._nominal_PublishService = None  # type: unique symbol

class RTAnimationTracker:
    def __init__(self):
        self._nominal_RTAnimationTracker = None  # type: unique symbol
        self.Active = None  # type: bool
        self.EnableFallbackAudioInput = None  # type: bool
        self.SessionName = None  # type: str
        self.TrackerMode = None  # type: Enum.TrackerMode
        self.TrackerType = None  # type: Enum.TrackerType
        self.TrackerError = None  # type: RBXScriptSignal<(errorCode: Enum.TrackerError, msg: str) => void>
        self.TrackerPrompt = None  # type: RBXScriptSignal<(prompt: Enum.TrackerPromptEvent) => void>

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
        self.RemoteOnInvokeClient = None  # type: RBXScriptSignal<(id: float, arguments: unknown) => void>
        self.RemoteOnInvokeError = None  # type: RBXScriptSignal<(id: float, arguments: str) => void>
        self.RemoteOnInvokeServer = None  # type: RBXScriptSignal<(id: float, player: Player, arguments: unknown) => void>
        self.RemoteOnInvokeSuccess = None  # type: RBXScriptSignal<(id: float, arguments: unknown) => void>
        self.OnClientInvoke = None  # type: T | undefined
        self.OnServerInvoke = None  # type: ((player: Player, ...args: List(unknown)) => void) | undefined

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
        self.Length = None  # type: float

class RtMessagingService:
    def __init__(self):
        self._nominal_RtMessagingService = None  # type: unique symbol

class RunService:
    def __init__(self):
        self._nominal_RunService = None  # type: unique symbol
        self.Heartbeat = None  # type: RBXScriptSignal<(deltaTime: float) => void>
        self.PostSimulation = None  # type: RBXScriptSignal<(deltaTimeSim: float) => void>
        self.PreAnimation = None  # type: RBXScriptSignal<(deltaTimeSim: float) => void>
        self.PreRender = None  # type: RBXScriptSignal<(deltaTimeRender: float) => void>
        self.PreSimulation = None  # type: RBXScriptSignal<(deltaTimeSim: float) => void>
        self.RenderStepped = None  # type: RBXScriptSignal<(deltaTime: float) => void>
        self.Stepped = None  # type: RBXScriptSignal<(time: float, deltaTime: float) => void>

class SafetyService:
    def __init__(self):
        self._nominal_SafetyService = None  # type: unique symbol

class ScreenshotHud:
    def __init__(self):
        self._nominal_ScreenshotHud = None  # type: unique symbol
        self.CameraButtonIcon = None  # type: ContentId
        self.CameraButtonPosition = None  # type: UDim2
        self.CloseButtonPosition = None  # type: UDim2
        self.CloseWhenScreenshotTaken = None  # type: bool
        self.ExperienceNameOverlayEnabled = None  # type: bool
        self.HideCoreGuiForCaptures = None  # type: bool
        self.HidePlayerGuiForCaptures = None  # type: bool
        self.OverlayFont = None  # type: Enum.Font
        self.UsernameOverlayEnabled = None  # type: bool
        self.Visible = None  # type: bool

class ScriptBuilder:
    def __init__(self):
        self._nominal_ScriptBuilder = None  # type: unique symbol

class SyncScriptBuilder:
    def __init__(self):
        self._nominal_SyncScriptBuilder = None  # type: unique symbol
        self.CompileTarget = None  # type: Enum.CompileTarget
        self.CoverageInfo = None  # type: bool
        self.DebugInfo = None  # type: bool
        self.PackAsSource = None  # type: bool
        self.RawBytecode = None  # type: bool

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
        self.Error = None  # type: RBXScriptSignal<(message: str, stackTrace: str, script?: LuaSourceContainer) => void>

class ScriptProfilerService:
    def __init__(self):
        self._nominal_ScriptProfilerService = None  # type: unique symbol

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
        self.UpdateType = None  # type: Enum.SensorUpdateType
        self.OnSensorOutputChanged = None  # type: RBXScriptSignal<() => void>

class AtmosphereSensor:
    def __init__(self):
        self._nominal_AtmosphereSensor = None  # type: unique symbol
        self.AirDensity = None  # type: float
        self.RelativeWindVelocity = None  # type: Vector3

class BuoyancySensor:
    def __init__(self):
        self._nominal_BuoyancySensor = None  # type: unique symbol
        self.FullySubmerged = None  # type: bool
        self.TouchingSurface = None  # type: bool

class ControllerSensor:
    def __init__(self):
        self._nominal_ControllerSensor = None  # type: unique symbol

class ControllerPartSensor:
    def __init__(self):
        self._nominal_ControllerPartSensor = None  # type: unique symbol
        self.HitFrame = None  # type: CFrame
        self.HitNormal = None  # type: Vector3
        self.SearchDistance = None  # type: float
        self.SensedPart = None  # type: BasePart | undefined
        self.SensorMode = None  # type: Enum.SensorMode

class FluidForceSensor:
    def __init__(self):
        self._nominal_FluidForceSensor = None  # type: unique symbol
        self.CenterOfPressure = None  # type: Vector3
        self.Force = None  # type: Vector3
        self.Torque = None  # type: Vector3

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
        self.Close = None  # type: RBXScriptSignal<() => void>
        self.ServiceAdded = None  # type: RBXScriptSignal<(service: S(keyof S)) => void>
        self.ServiceRemoving = None  # type: RBXScriptSignal<(service: S(keyof S)) => void>

class DataModel:
    def __init__(self):
        self._nominal_DataModel = None  # type: unique symbol
        self.CreatorId = None  # type: float
        self.CreatorType = None  # type: Enum.CreatorType
        self.GameId = None  # type: float
        self.GearGenreSetting = None  # type: Enum.GearGenreSetting
        self.Genre = None  # type: Enum.Genre
        self.JobId = None  # type: str
        self.MatchmakingType = None  # type: Enum.MatchmakingType
        self.PlaceId = None  # type: float
        self.PlaceVersion = None  # type: float
        self.PrivateServerId = None  # type: str
        self.PrivateServerOwnerId = None  # type: float
        self.VIPServerId = None  # type: str
        self.VIPServerOwnerId = None  # type: float
        self.Workspace = None  # type: Workspace
        self.AllowedGearTypeChanged = None  # type: RBXScriptSignal<() => void>
        self.GraphicsQualityChangeRequest = None  # type: RBXScriptSignal<(betterQuality: bool) => void>
        self.ItemChanged = None  # type: RBXScriptSignal<(object: Instance, descriptor: str) => void>
        self.Loaded = None  # type: RBXScriptSignal<() => void>
        self.OnClose = None  # type: (() => unknown) | undefined

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
        self.CelestialBodiesShown = None  # type: bool
        self.MoonAngularSize = None  # type: float
        self.MoonTextureId = None  # type: ContentId
        self.SkyboxBk = None  # type: ContentId
        self.SkyboxDn = None  # type: ContentId
        self.SkyboxFt = None  # type: ContentId
        self.SkyboxLf = None  # type: ContentId
        self.SkyboxOrientation = None  # type: Vector3
        self.SkyboxRt = None  # type: ContentId
        self.SkyboxUp = None  # type: ContentId
        self.StarCount = None  # type: float
        self.SunAngularSize = None  # type: float
        self.SunTextureId = None  # type: ContentId

class Smoke:
    def __init__(self):
        self._nominal_Smoke = None  # type: unique symbol
        self.Color = None  # type: Color3
        self.Enabled = None  # type: bool
        self.LocalTransparencyModifier = None  # type: float
        self.Opacity = None  # type: float
        self.RiseVelocity = None  # type: float
        self.Size = None  # type: float
        self.TimeScale = None  # type: float

class SmoothVoxelsUpgraderService:
    def __init__(self):
        self._nominal_SmoothVoxelsUpgraderService = None  # type: unique symbol

class SnippetService:
    def __init__(self):
        self._nominal_SnippetService = None  # type: unique symbol

class SocialService:
    def __init__(self):
        self._nominal_SocialService = None  # type: unique symbol
        self.CallInviteStateChanged = None  # type: RBXScriptSignal<(player: Player, inviteState: Enum.InviteState) => void>
        self.GameInvitePromptClosed = None  # type: RBXScriptSignal<(senderPlayer: Player, recipientIds: List(float)) => void>
        self.PhoneBookPromptClosed = None  # type: RBXScriptSignal<(player: Player) => void>
        self.OnCallInviteInvoked = None  # type: ((tag: str, callParticipantIds: List(unknown)) => Instance) | undefined

class Sound:
    def __init__(self):
        self._nominal_Sound = None  # type: unique symbol
        self.EmitterSize = None  # type: float
        self.IsLoaded = None  # type: bool
        self.IsPaused = None  # type: bool
        self.IsPlaying = None  # type: bool
        self.LoopRegion = None  # type: NumberRange
        self.Looped = None  # type: bool
        self.MaxDistance = None  # type: float
        self.MinDistance = None  # type: float
        self.Pitch = None  # type: float
        self.PlayOnRemove = None  # type: bool
        self.PlaybackLoudness = None  # type: float
        self.PlaybackRegion = None  # type: NumberRange
        self.PlaybackRegionsEnabled = None  # type: bool
        self.PlaybackSpeed = None  # type: float
        self.Playing = None  # type: bool
        self.RollOffMaxDistance = None  # type: float
        self.RollOffMinDistance = None  # type: float
        self.RollOffMode = None  # type: Enum.RollOffMode
        self.SoundGroup = None  # type: SoundGroup | undefined
        self.SoundId = None  # type: ContentId
        self.TimeLength = None  # type: float
        self.TimePosition = None  # type: float
        self.Volume = None  # type: float
        self.DidLoop = None  # type: RBXScriptSignal<(soundId: str, numOfTimesLooped: float) => void>
        self.Ended = None  # type: RBXScriptSignal<(soundId: str) => void>
        self.Loaded = None  # type: RBXScriptSignal<(soundId: str) => void>
        self.Paused = None  # type: RBXScriptSignal<(soundId: str) => void>
        self.Played = None  # type: RBXScriptSignal<(soundId: str) => void>
        self.Resumed = None  # type: RBXScriptSignal<(soundId: str) => void>
        self.Stopped = None  # type: RBXScriptSignal<(soundId: str) => void>

class SoundEffect:
    def __init__(self):
        self._nominal_SoundEffect = None  # type: unique symbol
        self.Enabled = None  # type: bool
        self.Priority = None  # type: float

class ChorusSoundEffect:
    def __init__(self):
        self._nominal_ChorusSoundEffect = None  # type: unique symbol
        self.Depth = None  # type: float
        self.Mix = None  # type: float
        self.Rate = None  # type: float

class CompressorSoundEffect:
    def __init__(self):
        self._nominal_CompressorSoundEffect = None  # type: unique symbol
        self.Attack = None  # type: float
        self.GainMakeup = None  # type: float
        self.Ratio = None  # type: float
        self.Release = None  # type: float
        self.SideChain = None  # type: Sound | SoundGroup | undefined
        self.Threshold = None  # type: float

class CustomSoundEffect:
    def __init__(self):
        self._nominal_CustomSoundEffect = None  # type: unique symbol

class AssetSoundEffect:
    def __init__(self):
        self._nominal_AssetSoundEffect = None  # type: unique symbol

class ChannelSelectorSoundEffect:
    def __init__(self):
        self._nominal_ChannelSelectorSoundEffect = None  # type: unique symbol
        self.Channel = None  # type: float

class DistortionSoundEffect:
    def __init__(self):
        self._nominal_DistortionSoundEffect = None  # type: unique symbol
        self.Level = None  # type: float

class EchoSoundEffect:
    def __init__(self):
        self._nominal_EchoSoundEffect = None  # type: unique symbol
        self.Delay = None  # type: float
        self.DryLevel = None  # type: float
        self.Feedback = None  # type: float
        self.WetLevel = None  # type: float

class EqualizerSoundEffect:
    def __init__(self):
        self._nominal_EqualizerSoundEffect = None  # type: unique symbol
        self.HighGain = None  # type: float
        self.LowGain = None  # type: float
        self.MidGain = None  # type: float

class FlangeSoundEffect:
    def __init__(self):
        self._nominal_FlangeSoundEffect = None  # type: unique symbol
        self.Depth = None  # type: float
        self.Mix = None  # type: float
        self.Rate = None  # type: float

class PitchShiftSoundEffect:
    def __init__(self):
        self._nominal_PitchShiftSoundEffect = None  # type: unique symbol
        self.Octave = None  # type: float

class ReverbSoundEffect:
    def __init__(self):
        self._nominal_ReverbSoundEffect = None  # type: unique symbol
        self.DecayTime = None  # type: float
        self.Density = None  # type: float
        self.Diffusion = None  # type: float
        self.DryLevel = None  # type: float
        self.WetLevel = None  # type: float

class TremoloSoundEffect:
    def __init__(self):
        self._nominal_TremoloSoundEffect = None  # type: unique symbol
        self.Depth = None  # type: float
        self.Duty = None  # type: float
        self.Frequency = None  # type: float

class SoundGroup:
    def __init__(self):
        self._nominal_SoundGroup = None  # type: unique symbol
        self.Volume = None  # type: float

class SoundService:
    def __init__(self):
        self._nominal_SoundService = None  # type: unique symbol
        self.AmbientReverb = None  # type: Enum.ReverbType
        self.DistanceFactor = None  # type: float
        self.DopplerScale = None  # type: float
        self.RespectFilteringEnabled = None  # type: bool
        self.RolloffScale = None  # type: float

class Sparkles:
    def __init__(self):
        self._nominal_Sparkles = None  # type: unique symbol
        self.Color = None  # type: Color3
        self.Enabled = None  # type: bool
        self.LocalTransparencyModifier = None  # type: float
        self.SparkleColor = None  # type: Color3
        self.TimeScale = None  # type: float

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
        self.AutoJumpEnabled = None  # type: bool
        self.CameraMaxZoomDistance = None  # type: float
        self.CameraMinZoomDistance = None  # type: float
        self.CameraMode = None  # type: Enum.CameraMode
        self.CharacterJumpHeight = None  # type: float
        self.CharacterJumpPower = None  # type: float
        self.CharacterMaxSlopeAngle = None  # type: float
        self.CharacterUseJumpPower = None  # type: bool
        self.CharacterWalkSpeed = None  # type: float
        self.ClassicDeath = None  # type: bool
        self.DevCameraOcclusionMode = None  # type: Enum.DevCameraOcclusionMode
        self.DevComputerCameraMovementMode = None  # type: Enum.DevComputerCameraMovementMode
        self.DevComputerMovementMode = None  # type: Enum.DevComputerMovementMode
        self.DevTouchCameraMovementMode = None  # type: Enum.DevTouchCameraMovementMode
        self.DevTouchMovementMode = None  # type: Enum.DevTouchMovementMode
        self.EnableMouseLockOption = None  # type: bool
        self.HealthDisplayDistance = None  # type: float
        self.LoadCharacterAppearance = None  # type: bool
        self.LuaCharacterController = None  # type: Enum.CharacterControlMode
        self.NameDisplayDistance = None  # type: float
        self.RagdollDeath = None  # type: bool
        self.UserEmotesEnabled = None  # type: bool

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
        self.ContactsCount = None  # type: float
        self.DataReceiveKbps = None  # type: float
        self.DataSendKbps = None  # type: float
        self.FrameTime = None  # type: float
        self.HeartbeatTime = None  # type: float
        self.HeartbeatTimeMs = None  # type: float
        self.InstanceCount = None  # type: float
        self.MovingPrimitivesCount = None  # type: float
        self.PhysicsReceiveKbps = None  # type: float
        self.PhysicsSendKbps = None  # type: float
        self.PhysicsStepTime = None  # type: float
        self.PhysicsStepTimeMs = None  # type: float
        self.PrimitivesCount = None  # type: float
        self.RenderCPUFrameTime = None  # type: float
        self.RenderGPUFrameTime = None  # type: float
        self.SceneDrawcallCount = None  # type: float
        self.SceneTriangleCount = None  # type: float
        self.ShadowsDrawcallCount = None  # type: float
        self.ShadowsTriangleCount = None  # type: float
        self.UI2DDrawcallCount = None  # type: float
        self.UI2DTriangleCount = None  # type: float
        self.UI3DDrawcallCount = None  # type: float
        self.UI3DTriangleCount = None  # type: float

class StreamingService:
    def __init__(self):
        self._nominal_StreamingService = None  # type: unique symbol

class StudioAssetService:
    def __init__(self):
        self._nominal_StudioAssetService = None  # type: unique symbol

class StudioAttachment:
    def __init__(self):
        self._nominal_StudioAttachment = None  # type: unique symbol
        self.AutoHideParent = None  # type: bool
        self.IsArrowVisible = None  # type: bool
        self.Offset = None  # type: Vector2
        self.SourceAnchorPoint = None  # type: Vector2
        self.TargetAnchorPoint = None  # type: Vector2

class StudioCallout:
    def __init__(self):
        self._nominal_StudioCallout = None  # type: unique symbol

class StudioCameraService:
    def __init__(self):
        self._nominal_StudioCameraService = None  # type: unique symbol
        self.LockCameraSpeed = None  # type: bool
        self.ShowCameraSpeed = None  # type: RBXScriptSignal<(speed: float) => void>

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
        self.StyleRulesChanged = None  # type: RBXScriptSignal<() => void>

class StyleRule:
    def __init__(self):
        self._nominal_StyleRule = None  # type: unique symbol
        self.Priority = None  # type: float
        self.Selector = None  # type: str
        self.SelectorError = None  # type: str

class StyleSheet:
    def __init__(self):
        self._nominal_StyleSheet = None  # type: unique symbol

class StyleDerive:
    def __init__(self):
        self._nominal_StyleDerive = None  # type: unique symbol
        self.Priority = None  # type: float
        self.StyleSheet = None  # type: StyleSheet | undefined

class StyleLink:
    def __init__(self):
        self._nominal_StyleLink = None  # type: unique symbol
        self.StyleSheet = None  # type: StyleSheet | undefined

class StylingService:
    def __init__(self):
        self._nominal_StylingService = None  # type: unique symbol

class SurfaceAppearance:
    def __init__(self):
        self._nominal_SurfaceAppearance = None  # type: unique symbol
        self.Color = None  # type: Color3

class SystemThemeService:
    def __init__(self):
        self._nominal_SystemThemeService = None  # type: unique symbol

class Team:
    def __init__(self):
        self._nominal_Team = None  # type: unique symbol
        self.AutoAssignable = None  # type: bool
        self.AutoColorCharacters = None  # type: bool
        self.Score = None  # type: float
        self.TeamColor = None  # type: BrickColor
        self.PlayerAdded = None  # type: RBXScriptSignal<(player: Player) => void>
        self.PlayerRemoved = None  # type: RBXScriptSignal<(player: Player) => void>

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
        self.PrivateServerId = None  # type: str
        self.ReservedServerAccessCode = None  # type: str

class TeleportOptions:
    def __init__(self):
        self._nominal_TeleportOptions = None  # type: unique symbol
        self.ReservedServerAccessCode = None  # type: str
        self.ServerInstanceId = None  # type: str
        self.ShouldReserveServer = None  # type: bool

class TeleportService:
    def __init__(self):
        self._nominal_TeleportService = None  # type: unique symbol
        self.CustomizedTeleportUI = None  # type: bool
        self.LocalPlayerArrivedFromTeleport = None  # type: RBXScriptSignal<(loadingGui: ScreenGui, dataTable?: unknown) => void>
        self.TeleportInitFailed = None  # type: RBXScriptSignal<(player: Player, teleportResult: Enum.TeleportResult, errorMessage: str, placeId: float, teleportOptions: TeleportOptions) => void>

class TemporaryCageMeshProvider:
    def __init__(self):
        self._nominal_TemporaryCageMeshProvider = None  # type: unique symbol

class TemporaryScriptService:
    def __init__(self):
        self._nominal_TemporaryScriptService = None  # type: unique symbol

class TerrainDetail:
    def __init__(self):
        self._nominal_TerrainDetail = None  # type: unique symbol
        self.Face = None  # type: Enum.TerrainFace
        self.MaterialPattern = None  # type: Enum.MaterialPattern
        self.StudsPerTile = None  # type: float

class TerrainRegion:
    def __init__(self):
        self._nominal_TerrainRegion = None  # type: unique symbol
        self.IsSmooth = None  # type: bool
        self.SizeInCells = None  # type: Vector3

class TestService:
    def __init__(self):
        self._nominal_TestService = None  # type: unique symbol
        self.AutoRuns = None  # type: bool
        self.Description = None  # type: str
        self.ErrorCount = None  # type: float
        self.ExecuteWithStudioRun = None  # type: bool
        self.Is30FpsThrottleEnabled = None  # type: bool
        self.IsPhysicsEnvironmentalThrottled = None  # type: bool
        self.IsSleepAllowed = None  # type: bool
        self.NumberOfPlayers = None  # type: float
        self.SimulateSecondsLag = None  # type: float
        self.TestCount = None  # type: float
        self.ThrottlePhysicsToRealtime = None  # type: bool
        self.Timeout = None  # type: float
        self.WarnCount = None  # type: float
        self.ServerCollectConditionalResult = None  # type: RBXScriptSignal<(condition: bool, text: str, script: Instance, line: float) => void>
        self.ServerCollectResult = None  # type: RBXScriptSignal<(text: str, script: Instance, line: float) => void>

class TextBoxService:
    def __init__(self):
        self._nominal_TextBoxService = None  # type: unique symbol

class TextChannel:
    def __init__(self):
        self._nominal_TextChannel = None  # type: unique symbol
        self.DirectChatRequester = None  # type: Player | undefined
        self.MessageReceived = None  # type: RBXScriptSignal<(incomingMessage: TextChatMessage) => void>
        self.OnIncomingMessage = None  # type: (message: TextChatMessage) => TextChatMessageProperties | undefined
        self.ShouldDeliverCallback = None  # type: (message: TextChatMessage, textSource: TextSource) => bool

class TextChatCommand:
    def __init__(self):
        self._nominal_TextChatCommand = None  # type: unique symbol
        self.AutocompleteVisible = None  # type: bool
        self.Enabled = None  # type: bool
        self.PrimaryAlias = None  # type: str
        self.SecondaryAlias = None  # type: str
        self.Triggered = None  # type: RBXScriptSignal<(originTextSource: TextSource, unfilteredText: str) => void>

class TextChatConfigurations:
    def __init__(self):
        self._nominal_TextChatConfigurations = None  # type: unique symbol

class BubbleChatConfiguration:
    def __init__(self):
        self._nominal_BubbleChatConfiguration = None  # type: unique symbol
        self.AdorneeName = None  # type: str
        self.BackgroundColor3 = None  # type: Color3
        self.BackgroundTransparency = None  # type: float
        self.BubbleDuration = None  # type: float
        self.BubblesSpacing = None  # type: float
        self.Enabled = None  # type: bool
        self.Font = None  # type: Enum.Font
        self.FontFace = None  # type: Font
        self.LocalPlayerStudsOffset = None  # type: Vector3
        self.MaxBubbles = None  # type: float
        self.MaxDistance = None  # type: float
        self.MinimizeDistance = None  # type: float
        self.TailVisible = None  # type: bool
        self.TextColor3 = None  # type: Color3
        self.TextSize = None  # type: float
        self.VerticalStudsOffset = None  # type: float

class ChannelTabsConfiguration:
    def __init__(self):
        self._nominal_ChannelTabsConfiguration = None  # type: unique symbol
        self.AbsolutePosition = None  # type: Vector2
        self.AbsoluteSize = None  # type: Vector2
        self.BackgroundColor3 = None  # type: Color3
        self.BackgroundTransparency = None  # type: float
        self.Enabled = None  # type: bool
        self.FontFace = None  # type: Font
        self.HoverBackgroundColor3 = None  # type: Color3
        self.SelectedTabTextColor3 = None  # type: Color3
        self.TextColor3 = None  # type: Color3
        self.TextSize = None  # type: float
        self.TextStrokeColor3 = None  # type: Color3
        self.TextStrokeTransparency = None  # type: float

class ChatInputBarConfiguration:
    def __init__(self):
        self._nominal_ChatInputBarConfiguration = None  # type: unique symbol
        self.AbsolutePosition = None  # type: Vector2
        self.AbsoluteSize = None  # type: Vector2
        self.AutocompleteEnabled = None  # type: bool
        self.BackgroundColor3 = None  # type: Color3
        self.BackgroundTransparency = None  # type: float
        self.Enabled = None  # type: bool
        self.FontFace = None  # type: Font
        self.IsFocused = None  # type: bool
        self.KeyboardKeyCode = None  # type: Enum.KeyCode
        self.PlaceholderColor3 = None  # type: Color3
        self.TargetTextChannel = None  # type: TextChannel | undefined
        self.TextBox = None  # type: TextBox | undefined
        self.TextColor3 = None  # type: Color3
        self.TextSize = None  # type: float
        self.TextStrokeColor3 = None  # type: Color3
        self.TextStrokeTransparency = None  # type: float

class ChatWindowConfiguration:
    def __init__(self):
        self._nominal_ChatWindowConfiguration = None  # type: unique symbol
        self.AbsolutePosition = None  # type: Vector2
        self.AbsoluteSize = None  # type: Vector2
        self.BackgroundColor3 = None  # type: Color3
        self.BackgroundTransparency = None  # type: float
        self.Enabled = None  # type: bool
        self.FontFace = None  # type: Font
        self.HeightScale = None  # type: float
        self.HorizontalAlignment = None  # type: Enum.HorizontalAlignment
        self.TextColor3 = None  # type: Color3
        self.TextSize = None  # type: float
        self.TextStrokeColor3 = None  # type: Color3
        self.TextStrokeTransparency = None  # type: float
        self.VerticalAlignment = None  # type: Enum.VerticalAlignment
        self.WidthScale = None  # type: float

class TextChatMessage:
    def __init__(self):
        self._nominal_TextChatMessage = None  # type: unique symbol
        self.BubbleChatMessageProperties = None  # type: BubbleChatMessageProperties | undefined
        self.ChatWindowMessageProperties = None  # type: ChatWindowMessageProperties | undefined
        self.MessageId = None  # type: str
        self.Metadata = None  # type: str
        self.PrefixText = None  # type: str
        self.Status = None  # type: Enum.TextChatMessageStatus
        self.Text = None  # type: str
        self.TextChannel = None  # type: TextChannel | undefined
        self.TextSource = None  # type: TextSource | undefined
        self.Timestamp = None  # type: DateTime
        self.Translation = None  # type: str

class TextChatMessageProperties:
    def __init__(self):
        self._nominal_TextChatMessageProperties = None  # type: unique symbol
        self.PrefixText = None  # type: str
        self.Text = None  # type: str
        self.Translation = None  # type: str

class BubbleChatMessageProperties:
    def __init__(self):
        self._nominal_BubbleChatMessageProperties = None  # type: unique symbol
        self.BackgroundColor3 = None  # type: Color3
        self.BackgroundTransparency = None  # type: float
        self.FontFace = None  # type: Font
        self.TailVisible = None  # type: bool
        self.TextColor3 = None  # type: Color3
        self.TextSize = None  # type: float

class ChatWindowMessageProperties:
    def __init__(self):
        self._nominal_ChatWindowMessageProperties = None  # type: unique symbol
        self.FontFace = None  # type: Font
        self.PrefixTextProperties = None  # type: ChatWindowMessageProperties | undefined
        self.TextColor3 = None  # type: Color3
        self.TextSize = None  # type: float
        self.TextStrokeColor3 = None  # type: Color3
        self.TextStrokeTransparency = None  # type: float

class TextChatService:
    def __init__(self):
        self._nominal_TextChatService = None  # type: unique symbol
        self.BubbleDisplayed = None  # type: RBXScriptSignal<(partOrCharacter: Instance, textChatMessage: TextChatMessage) => void>
        self.MessageReceived = None  # type: RBXScriptSignal<(textChatMessage: TextChatMessage) => void>
        self.SendingMessage = None  # type: RBXScriptSignal<(textChatMessage: TextChatMessage) => void>
        self.OnBubbleAdded = None  # type: (message: TextChatMessage, adornee: Instance) => BubbleChatMessageProperties | undefined
        self.OnChatWindowAdded = None  # type: (message: TextChatMessage) => ChatWindowMessageProperties | undefined
        self.OnIncomingMessage = None  # type: (message: TextChatMessage) => TextChatMessageProperties | undefined

class TextFilterResult:
    def __init__(self):
        self._nominal_TextFilterResult = None  # type: unique symbol

class TextFilterTranslatedResult:
    def __init__(self):
        self._nominal_TextFilterTranslatedResult = None  # type: unique symbol
        self.SourceLanguage = None  # type: str
        self.SourceText = None  # type: TextFilterResult | undefined

class TextService:
    def __init__(self):
        self._nominal_TextService = None  # type: unique symbol

class TextSource:
    def __init__(self):
        self._nominal_TextSource = None  # type: unique symbol
        self.CanSend = None  # type: bool
        self.UserId = None  # type: float

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
        self.AudioMode = None  # type: Enum.TrackerLodFlagMode
        self.VideoExtrapolationMode = None  # type: Enum.TrackerExtrapolationFlagMode
        self.VideoLodMode = None  # type: Enum.TrackerLodValueMode
        self.VideoMode = None  # type: Enum.TrackerLodFlagMode

class TrackerStreamAnimation:
    def __init__(self):
        self._nominal_TrackerStreamAnimation = None  # type: unique symbol

class Trail:
    def __init__(self):
        self._nominal_Trail = None  # type: unique symbol
        self.Attachment0 = None  # type: Attachment | undefined
        self.Attachment1 = None  # type: Attachment | undefined
        self.Brightness = None  # type: float
        self.Color = None  # type: ColorSequence
        self.Enabled = None  # type: bool
        self.FaceCamera = None  # type: bool
        self.Lifetime = None  # type: float
        self.LightEmission = None  # type: float
        self.LightInfluence = None  # type: float
        self.LocalTransparencyModifier = None  # type: float
        self.MaxLength = None  # type: float
        self.MinLength = None  # type: float
        self.Texture = None  # type: ContentId
        self.TextureLength = None  # type: float
        self.TextureMode = None  # type: Enum.TextureMode
        self.Transparency = None  # type: NumberSequence
        self.WidthScale = None  # type: NumberSequence
        self.OnClearRequested = None  # type: RBXScriptSignal<() => void>

class Translator:
    def __init__(self):
        self._nominal_Translator = None  # type: unique symbol
        self.LocaleId = None  # type: str

class TutorialService:
    def __init__(self):
        self._nominal_TutorialService = None  # type: unique symbol

class TweenBase:
    def __init__(self):
        self._nominal_TweenBase = None  # type: unique symbol
        self.PlaybackState = None  # type: Enum.PlaybackState
        self.Completed = None  # type: RBXScriptSignal<(playbackState: Enum.PlaybackState) => void>

class Tween:
    def __init__(self):
        self._nominal_Tween = None  # type: unique symbol
        self.Instance = None  # type: Instance | undefined
        self.TweenInfo = None  # type: TweenInfo

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
        self.AspectRatio = None  # type: float
        self.AspectType = None  # type: Enum.AspectType
        self.DominantAxis = None  # type: Enum.DominantAxis

class UISizeConstraint:
    def __init__(self):
        self._nominal_UISizeConstraint = None  # type: unique symbol
        self.MaxSize = None  # type: Vector2
        self.MinSize = None  # type: Vector2

class UITextSizeConstraint:
    def __init__(self):
        self._nominal_UITextSizeConstraint = None  # type: unique symbol
        self.MaxTextSize = None  # type: float
        self.MinTextSize = None  # type: float

class UICorner:
    def __init__(self):
        self._nominal_UICorner = None  # type: unique symbol
        self.CornerRadius = None  # type: UDim

class UIDragDetector:
    def __init__(self):
        self._nominal_UIDragDetector = None  # type: unique symbol
        self.ActivatedCursorIcon = None  # type: ContentId
        self.BoundingBehavior = None  # type: Enum.UIDragDetectorBoundingBehavior
        self.BoundingUI = None  # type: GuiBase2d | undefined
        self.CursorIcon = None  # type: ContentId
        self.DragAxis = None  # type: Vector2
        self.DragRelativity = None  # type: Enum.UIDragDetectorDragRelativity
        self.DragRotation = None  # type: float
        self.DragSpace = None  # type: Enum.UIDragDetectorDragSpace
        self.DragStyle = None  # type: Enum.UIDragDetectorDragStyle
        self.DragUDim2 = None  # type: UDim2
        self.Enabled = None  # type: bool
        self.MaxDragAngle = None  # type: float
        self.MaxDragTranslation = None  # type: UDim2
        self.MinDragAngle = None  # type: float
        self.MinDragTranslation = None  # type: UDim2
        self.ReferenceUIInstance = None  # type: GuiObject | undefined
        self.ResponseStyle = None  # type: Enum.UIDragDetectorResponseStyle
        self.SelectionModeDragSpeed = None  # type: UDim2
        self.SelectionModeRotateSpeed = None  # type: float
        self.UIDragSpeedAxisMapping = None  # type: Enum.UIDragSpeedAxisMapping
        self.DragContinue = None  # type: RBXScriptSignal<(inputPosition: Vector2) => void>
        self.DragEnd = None  # type: RBXScriptSignal<(inputPosition: Vector2) => void>
        self.DragStart = None  # type: RBXScriptSignal<(inputPosition: Vector2) => void>

class UIFlexItem:
    def __init__(self):
        self._nominal_UIFlexItem = None  # type: unique symbol
        self.FlexMode = None  # type: Enum.UIFlexMode
        self.GrowRatio = None  # type: float
        self.ItemLineAlignment = None  # type: Enum.ItemLineAlignment
        self.ShrinkRatio = None  # type: float

class UIGradient:
    def __init__(self):
        self._nominal_UIGradient = None  # type: unique symbol
        self.Color = None  # type: ColorSequence
        self.Enabled = None  # type: bool
        self.Offset = None  # type: Vector2
        self.Rotation = None  # type: float
        self.Transparency = None  # type: NumberSequence

class UILayout:
    def __init__(self):
        self._nominal_UILayout = None  # type: unique symbol

class UIGridStyleLayout:
    def __init__(self):
        self._nominal_UIGridStyleLayout = None  # type: unique symbol
        self.AbsoluteContentSize = None  # type: Vector2
        self.FillDirection = None  # type: Enum.FillDirection
        self.HorizontalAlignment = None  # type: Enum.HorizontalAlignment
        self.SortOrder = None  # type: Enum.SortOrder
        self.VerticalAlignment = None  # type: Enum.VerticalAlignment

class UIGridLayout:
    def __init__(self):
        self._nominal_UIGridLayout = None  # type: unique symbol
        self.AbsoluteCellCount = None  # type: Vector2
        self.AbsoluteCellSize = None  # type: Vector2
        self.CellPadding = None  # type: UDim2
        self.CellSize = None  # type: UDim2
        self.FillDirectionMaxCells = None  # type: float
        self.StartCorner = None  # type: Enum.StartCorner

class UIListLayout:
    def __init__(self):
        self._nominal_UIListLayout = None  # type: unique symbol
        self.HorizontalFlex = None  # type: Enum.UIFlexAlignment
        self.ItemLineAlignment = None  # type: Enum.ItemLineAlignment
        self.Padding = None  # type: UDim
        self.VerticalFlex = None  # type: Enum.UIFlexAlignment
        self.Wraps = None  # type: bool

class UIPageLayout:
    def __init__(self):
        self._nominal_UIPageLayout = None  # type: unique symbol
        self.Animated = None  # type: bool
        self.Circular = None  # type: bool
        self.CurrentPage = None  # type: GuiObject | undefined
        self.EasingDirection = None  # type: Enum.EasingDirection
        self.EasingStyle = None  # type: Enum.EasingStyle
        self.GamepadInputEnabled = None  # type: bool
        self.Padding = None  # type: UDim
        self.ScrollWheelInputEnabled = None  # type: bool
        self.TouchInputEnabled = None  # type: bool
        self.TweenTime = None  # type: float
        self.PageEnter = None  # type: RBXScriptSignal<(page: GuiObject) => void>
        self.PageLeave = None  # type: RBXScriptSignal<(page: GuiObject) => void>
        self.Stopped = None  # type: RBXScriptSignal<(page: GuiObject) => void>

class UITableLayout:
    def __init__(self):
        self._nominal_UITableLayout = None  # type: unique symbol
        self.FillEmptySpaceColumns = None  # type: bool
        self.FillEmptySpaceRows = None  # type: bool
        self.MajorAxis = None  # type: Enum.TableMajorAxis
        self.Padding = None  # type: UDim2

class UIPadding:
    def __init__(self):
        self._nominal_UIPadding = None  # type: unique symbol
        self.PaddingBottom = None  # type: UDim
        self.PaddingLeft = None  # type: UDim
        self.PaddingRight = None  # type: UDim
        self.PaddingTop = None  # type: UDim

class UIScale:
    def __init__(self):
        self._nominal_UIScale = None  # type: unique symbol
        self.Scale = None  # type: float

class UIStroke:
    def __init__(self):
        self._nominal_UIStroke = None  # type: unique symbol
        self.ApplyStrokeMode = None  # type: Enum.ApplyStrokeMode
        self.Color = None  # type: Color3
        self.Enabled = None  # type: bool
        self.LineJoinMode = None  # type: Enum.LineJoinMode
        self.Thickness = None  # type: float
        self.Transparency = None  # type: float

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
        self.ComputerCameraMovementMode = None  # type: Enum.ComputerCameraMovementMode
        self.ComputerMovementMode = None  # type: Enum.ComputerMovementMode
        self.ControlMode = None  # type: Enum.ControlMode
        self.GamepadCameraSensitivity = None  # type: float
        self.MouseSensitivity = None  # type: float
        self.RCCProfilerRecordFrameRate = None  # type: float
        self.RCCProfilerRecordTimeFrame = None  # type: float
        self.RotationType = None  # type: Enum.RotationType
        self.SavedQualityLevel = None  # type: Enum.SavedQualitySetting
        self.TouchCameraMovementMode = None  # type: Enum.TouchCameraMovementMode
        self.TouchMovementMode = None  # type: Enum.TouchMovementMode
        self.FullscreenChanged = None  # type: RBXScriptSignal<(isFullscreen: bool) => void>
        self.StudioModeChanged = None  # type: RBXScriptSignal<(isStudioMode: bool) => void>

class UserInputService:
    def __init__(self):
        self._nominal_UserInputService = None  # type: unique symbol
        self.AccelerometerEnabled = None  # type: bool
        self.GamepadEnabled = None  # type: bool
        self.GyroscopeEnabled = None  # type: bool
        self.KeyboardEnabled = None  # type: bool
        self.ModalEnabled = None  # type: bool
        self.MouseBehavior = None  # type: Enum.MouseBehavior
        self.MouseDeltaSensitivity = None  # type: float
        self.MouseEnabled = None  # type: bool
        self.MouseIcon = None  # type: ContentId
        self.MouseIconEnabled = None  # type: bool
        self.OnScreenKeyboardPosition = None  # type: Vector2
        self.OnScreenKeyboardSize = None  # type: Vector2
        self.OnScreenKeyboardVisible = None  # type: bool
        self.TouchEnabled = None  # type: bool
        self.UserHeadCFrame = None  # type: CFrame
        self.VREnabled = None  # type: bool
        self.DeviceAccelerationChanged = None  # type: RBXScriptSignal<(acceleration: InputObject) => void>
        self.DeviceGravityChanged = None  # type: RBXScriptSignal<(gravity: InputObject) => void>
        self.DeviceRotationChanged = None  # type: RBXScriptSignal<(rotation: InputObject, cframe: CFrame) => void>
        self.GamepadConnected = None  # type: RBXScriptSignal<(gamepadNum: Enum.UserInputType) => void>
        self.GamepadDisconnected = None  # type: RBXScriptSignal<(gamepadNum: Enum.UserInputType) => void>
        self.InputBegan = None  # type: RBXScriptSignal<(input: InputObject, gameProcessedEvent: bool) => void>
        self.InputChanged = None  # type: RBXScriptSignal<(input: InputObject, gameProcessedEvent: bool) => void>
        self.InputEnded = None  # type: RBXScriptSignal<(input: InputObject, gameProcessedEvent: bool) => void>
        self.JumpRequest = None  # type: RBXScriptSignal<() => void>
        self.LastInputTypeChanged = None  # type: RBXScriptSignal<(lastInputType: Enum.UserInputType) => void>
        self.PointerAction = None  # type: RBXScriptSignal<(wheel: float, pan: Vector2, pinch: float, gameProcessedEvent: bool) => void>
        self.TextBoxFocusReleased = None  # type: RBXScriptSignal<(textboxReleased: TextBox) => void>
        self.TextBoxFocused = None  # type: RBXScriptSignal<(textboxFocused: TextBox) => void>
        self.TouchDrag = None  # type: RBXScriptSignal<(dragDirection: Enum.SwipeDirection, numberOfTouches: float, gameProcessedEvent: bool) => void>
        self.TouchEnded = None  # type: RBXScriptSignal<(touch: InputObject, gameProcessedEvent: bool) => void>
        self.TouchLongPress = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), state: Enum.UserInputState, gameProcessedEvent: bool) => void>
        self.TouchMoved = None  # type: RBXScriptSignal<(touch: InputObject, gameProcessedEvent: bool) => void>
        self.TouchPan = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), totalTranslation: Vector2, velocity: Vector2, state: Enum.UserInputState, gameProcessedEvent: bool) => void>
        self.TouchPinch = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), scale: float, velocity: float, state: Enum.UserInputState, gameProcessedEvent: bool) => void>
        self.TouchRotate = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), rotation: float, velocity: float, state: Enum.UserInputState, gameProcessedEvent: bool) => void>
        self.TouchStarted = None  # type: RBXScriptSignal<(touch: InputObject, gameProcessedEvent: bool) => void>
        self.TouchSwipe = None  # type: RBXScriptSignal<(swipeDirection: Enum.SwipeDirection, numberOfTouches: float, gameProcessedEvent: bool) => void>
        self.TouchTap = None  # type: RBXScriptSignal<(touchPositions: List(Vector2), gameProcessedEvent: bool) => void>
        self.TouchTapInWorld = None  # type: RBXScriptSignal<(position: Vector2, processedByUI: bool) => void>
        self.UserCFrameChanged = None  # type: RBXScriptSignal<(type: Enum.UserCFrame, value: CFrame) => void>
        self.WindowFocusReleased = None  # type: RBXScriptSignal<() => void>
        self.WindowFocused = None  # type: RBXScriptSignal<() => void>

class UserService:
    def __init__(self):
        self._nominal_UserService = None  # type: unique symbol

class VRService:
    def __init__(self):
        self._nominal_VRService = None  # type: unique symbol
        self.AutomaticScaling = None  # type: Enum.VRScaling
        self.AvatarGestures = None  # type: bool
        self.ControllerModels = None  # type: Enum.VRControllerModelMode
        self.FadeOutViewOnCollision = None  # type: bool
        self.GuiInputUserCFrame = None  # type: Enum.UserCFrame
        self.LaserPointer = None  # type: Enum.VRLaserPointerMode
        self.ThirdPersonFollowCamEnabled = None  # type: bool
        self.VREnabled = None  # type: bool
        self.NavigationRequested = None  # type: RBXScriptSignal<(cframe: CFrame, inputUserCFrame: Enum.UserCFrame) => void>
        self.TouchpadModeChanged = None  # type: RBXScriptSignal<(pad: Enum.VRTouchpad, mode: Enum.VRTouchpadMode) => void>
        self.UserCFrameChanged = None  # type: RBXScriptSignal<(type: Enum.UserCFrame, value: CFrame) => void>
        self.UserCFrameEnabled = None  # type: RBXScriptSignal<(type: Enum.UserCFrame, enabled: bool) => void>

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
        self.Value = None  # type: bool
        self.Changed = None  # type: RBXScriptSignal<(value: bool) => void>

class BrickColorValue:
    def __init__(self):
        self._nominal_BrickColorValue = None  # type: unique symbol
        self.Value = None  # type: BrickColor
        self.Changed = None  # type: RBXScriptSignal<(value: BrickColor) => void>

class CFrameValue:
    def __init__(self):
        self._nominal_CFrameValue = None  # type: unique symbol
        self.Value = None  # type: CFrame
        self.Changed = None  # type: RBXScriptSignal<(value: CFrame) => void>

class Color3Value:
    def __init__(self):
        self._nominal_Color3Value = None  # type: unique symbol
        self.Value = None  # type: Color3
        self.Changed = None  # type: RBXScriptSignal<(value: Color3) => void>

class DoubleConstrainedValue:
    def __init__(self):
        self._nominal_DoubleConstrainedValue = None  # type: unique symbol
        self.ConstrainedValue = None  # type: float
        self.MaxValue = None  # type: float
        self.MinValue = None  # type: float
        self.Value = None  # type: float
        self.Changed = None  # type: RBXScriptSignal<(value: float) => void>

class IntConstrainedValue:
    def __init__(self):
        self._nominal_IntConstrainedValue = None  # type: unique symbol
        self.ConstrainedValue = None  # type: float
        self.MaxValue = None  # type: float
        self.MinValue = None  # type: float
        self.Value = None  # type: float
        self.Changed = None  # type: RBXScriptSignal<(value: float) => void>

class IntValue:
    def __init__(self):
        self._nominal_IntValue = None  # type: unique symbol
        self.Value = None  # type: float
        self.Changed = None  # type: RBXScriptSignal<(value: float) => void>

class NumberValue:
    def __init__(self):
        self._nominal_NumberValue = None  # type: unique symbol
        self.Value = None  # type: float
        self.Changed = None  # type: RBXScriptSignal<(value: float) => void>

class ObjectValue:
    def __init__(self):
        self._nominal_ObjectValue = None  # type: unique symbol
        self.Value = None  # type: Instance | undefined
        self.Changed = None  # type: RBXScriptSignal<(value?: Instance) => void>

class RayValue:
    def __init__(self):
        self._nominal_RayValue = None  # type: unique symbol
        self.Value = None  # type: Ray
        self.Changed = None  # type: RBXScriptSignal<(value: Ray) => void>

class StringValue:
    def __init__(self):
        self._nominal_StringValue = None  # type: unique symbol
        self.Value = None  # type: str
        self.Changed = None  # type: RBXScriptSignal<(value: str) => void>

class Vector3Value:
    def __init__(self):
        self._nominal_Vector3Value = None  # type: unique symbol
        self.Value = None  # type: Vector3
        self.Changed = None  # type: RBXScriptSignal<(value: Vector3) => void>

class Vector3Curve:
    def __init__(self):
        self._nominal_Vector3Curve = None  # type: unique symbol

class VideoCaptureService:
    def __init__(self):
        self._nominal_VideoCaptureService = None  # type: unique symbol

class VideoDeviceInput:
    def __init__(self):
        self._nominal_VideoDeviceInput = None  # type: unique symbol
        self.Active = None  # type: bool
        self.CameraId = None  # type: str
        self.CaptureQuality = None  # type: Enum.VideoDeviceCaptureQuality
        self.IsReady = None  # type: bool

class VideoPlayer:
    def __init__(self):
        self._nominal_VideoPlayer = None  # type: unique symbol
        self.Asset = None  # type: ContentId
        self.IsLoaded = None  # type: bool
        self.IsPlaying = None  # type: bool
        self.Looping = None  # type: bool
        self.PlaybackSpeed = None  # type: float
        self.Resolution = None  # type: Vector2
        self.TimeLength = None  # type: float
        self.TimePosition = None  # type: float
        self.Volume = None  # type: float
        self.DidEnd = None  # type: RBXScriptSignal<() => void>
        self.DidLoop = None  # type: RBXScriptSignal<() => void>
        self.PlayFailed = None  # type: RBXScriptSignal<(error: Enum.AssetFetchStatus) => void>
        self.WiringChanged = None  # type: RBXScriptSignal<(connected: bool, pin: str, wire: Wire, instance: Instance) => void>

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
        self.VoiceChatState = None  # type: Enum.VoiceChatState
        self.StateChanged = None  # type: RBXScriptSignal<(oldValue: Enum.VoiceChatState, newValue: Enum.VoiceChatState) => void>

class VoiceChatService:
    def __init__(self):
        self._nominal_VoiceChatService = None  # type: unique symbol

class WebSocketClient:
    def __init__(self):
        self._nominal_WebSocketClient = None  # type: unique symbol
        self.ConnectionState = None  # type: Enum.WebSocketState
        self.Closed = None  # type: RBXScriptSignal<() => void>
        self.MessageReceived = None  # type: RBXScriptSignal<(data: str) => void>
        self.Opened = None  # type: RBXScriptSignal<() => void>

class WebSocketService:
    def __init__(self):
        self._nominal_WebSocketService = None  # type: unique symbol

class WebViewService:
    def __init__(self):
        self._nominal_WebViewService = None  # type: unique symbol

class WeldConstraint:
    def __init__(self):
        self._nominal_WeldConstraint = None  # type: unique symbol
        self.Active = None  # type: bool
        self.Enabled = None  # type: bool
        self.Part0 = None  # type: BasePart | undefined
        self.Part1 = None  # type: BasePart | undefined

class Wire:
    def __init__(self):
        self._nominal_Wire = None  # type: unique symbol
        self.Connected = None  # type: bool
        self.SourceInstance = None  # type: Instance | undefined
        self.SourceName = None  # type: str
        self.TargetInstance = None  # type: Instance | undefined
        self.TargetName = None  # type: str
